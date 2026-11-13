import http.server
import socketserver
import urllib.parse
import sqlite3
import os
import sys

PORT = 8080
DB_FILE = "student_project.db"

# Initialize SQLite database matching database.sql
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ('Rahul Sharma', 85.5),
            ('Priya Patel', 92.0),
            ('Amit Kumar', 78.3),
            ('Sneha Gupta', 88.7),
            ('Vikram Singh', 91.2)
        ]
        cursor.executemany("INSERT INTO students (name, marks) VALUES (?, ?)", sample_data)
        conn.commit()
    conn.close()

def get_grade(marks):
    if marks >= 90.0:
        return 'A', 'success'
    elif marks >= 75.0:
        return 'B', 'primary'
    elif marks >= 50.0:
        return 'C', 'warning'
    else:
        return 'F', 'danger'

# In-memory simple session store
SESSIONS = set()

class StudentRequestHandler(http.server.BaseHTTPRequestHandler):
    def send_html(self, content, status=200, cookie=None):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def redirect(self, location, cookie=None):
        self.send_response(302)
        self.send_header('Location', location)
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()

    def is_authenticated(self):
        cookie_header = self.headers.get('Cookie')
        if cookie_header:
            cookies = [c.strip() for c in cookie_header.split(';')]
            for c in cookies:
                if c.startswith('session_admin='):
                    token = c.split('=', 1)[1]
                    if token in SESSIONS:
                        return True
        return False

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Route: Homepage / Login
        if path in ['/', '/login', '/login.jsp']:
            error_msg = query.get('error', [None])[0]
            err_html = ""
            if error_msg:
                err_html = f'''
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <i class="bi bi-exclamation-triangle-fill me-2"></i>Invalid username or password! Please try again.
                </div>'''
            
            with open("WebContent/login.jsp", "r", encoding="utf-8") as f:
                raw = f.read()
            # Replace JSP tags with HTML
            raw = raw.replace('<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>', '')
            raw = raw.replace('''    <% 
        String errorMessage = (String) request.getAttribute("errorMessage");
        if (errorMessage != null) { 
    %>
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <i class="bi bi-exclamation-triangle-fill me-2"></i><%= errorMessage %>
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    <% } %>''', err_html)
            self.send_html(raw)
            return

        # Route: Logout
        if path in ['/logout', '/logout.jsp']:
            cookie_header = self.headers.get('Cookie')
            if cookie_header:
                for c in cookie_header.split(';'):
                    if 'session_admin=' in c:
                        token = c.split('=', 1)[1].strip()
                        SESSIONS.discard(token)
            self.redirect('/login.jsp', cookie='session_admin=; Max-Age=0; Path=/')
            return

        # Protected Routes Check
        if not self.is_authenticated():
            self.redirect('/login.jsp')
            return

        # Route: Dashboard
        if path in ['/dashboard', '/dashboard.jsp']:
            with open("WebContent/dashboard.jsp", "r", encoding="utf-8") as f:
                raw = f.read()
            raw = raw.replace('<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>', '')
            raw = raw.replace('''<%
    // Session check — if not logged in, redirect to login page
    if (session.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    String user = (String) session.getAttribute("user");
%>''', '')
            raw = raw.replace('<%= user %>', 'admin')
            self.send_html(raw)
            return

        # Route: View All Students
        if path in ['/viewStudents', '/viewStudents.jsp']:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, marks FROM students ORDER BY id ASC")
            rows = cursor.fetchall()
            conn.close()

            table_rows_html = ""
            for rid, name, marks in rows:
                grade, badge_class = get_grade(marks)
                table_rows_html += f"""
                <tr>
                    <td class="text-center"><strong>{rid}</strong></td>
                    <td>{name}</td>
                    <td class="text-center">{marks:.2f}</td>
                    <td class="text-center"><span class="badge bg-{badge_class} fs-6">{grade}</span></td>
                    <td class="text-center">
                        <a href="updateStudent?id={rid}" class="btn btn-sm btn-outline-primary me-2"><i class="bi bi-pencil-square"></i> Edit</a>
                        <a href="deleteStudent?id={rid}" class="btn btn-sm btn-outline-danger" onclick="return confirm('Are you sure you want to delete {name}?');"><i class="bi bi-trash"></i> Delete</a>
                    </td>
                </tr>"""

            with open("WebContent/viewStudents.jsp", "r", encoding="utf-8") as f:
                raw = f.read()
            # Clean JSP scriptlet loop and replace with rows
            start_marker = "<%"
            end_marker = "%>"
            # Standard template replacement
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>View Students - Smart Student Management System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body style="background: #f0f2f5;">
    <nav class="navbar navbar-expand-lg navbar-dark" style="background: linear-gradient(135deg, #667eea, #764ba2);">
        <div class="container">
            <a class="navbar-brand fw-bold" href="dashboard.jsp"><i class="bi bi-mortarboard-fill me-2"></i>Student Management</a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link text-white me-3" href="dashboard.jsp"><i class="bi bi-speedometer2"></i> Dashboard</a>
                <a class="nav-link text-white me-3" href="addStudent.jsp"><i class="bi bi-person-plus-fill"></i> Add Student</a>
                <a class="nav-link text-white me-3" href="searchStudent.jsp"><i class="bi bi-search"></i> Search</a>
                <a class="nav-link text-white" href="logout"><i class="bi bi-box-arrow-right"></i> Logout</a>
            </div>
        </div>
    </nav>
    <div class="container my-5">
        <div class="card shadow-sm border-0 rounded-4 p-4 bg-white">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3 class="fw-bold mb-0 text-dark"><i class="bi bi-people-fill text-primary me-2"></i>All Registered Students</h3>
                <a href="addStudent.jsp" class="btn btn-primary"><i class="bi bi-plus-circle me-1"></i> Add New Student</a>
            </div>
            <div class="table-responsive">
                <table class="table table-hover align-middle">
                    <thead class="table-dark">
                        <tr><th class="text-center">ID</th><th>Full Name</th><th class="text-center">Marks</th><th class="text-center">Grade</th><th class="text-center">Actions</th></tr>
                    </thead>
                    <tbody>
                        {table_rows_html}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>"""
            self.send_html(html)
            return

        # Route: Add Student Form
        if path in ['/addStudent', '/addStudent.jsp']:
            with open("WebContent/addStudent.jsp", "r", encoding="utf-8") as f:
                raw = f.read()
            raw = raw.replace('<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>', '')
            raw = raw.replace('''<%
    if (session.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
%>''', '')
            self.send_html(raw)
            return

        # Route: Search Student Form
        if path in ['/searchStudent', '/searchStudent.jsp']:
            search_id = query.get('id', [None])[0]
            result_html = ""
            if search_id:
                try:
                    sid = int(search_id)
                    conn = sqlite3.connect(DB_FILE)
                    cursor = conn.cursor()
                    cursor.execute("SELECT id, name, marks FROM students WHERE id = ?", (sid,))
                    row = cursor.fetchone()
                    conn.close()
                    if row:
                        grade, badge = get_grade(row[2])
                        result_html = f'''
                        <div class="card shadow-sm border-0 rounded-4 p-4 mt-4 bg-light">
                            <h4 class="text-success"><i class="bi bi-check-circle-fill me-2"></i>Student Record Found</h4>
                            <p class="mb-1"><strong>ID:</strong> {row[0]}</p>
                            <p class="mb-1"><strong>Name:</strong> {row[1]}</p>
                            <p class="mb-1"><strong>Marks:</strong> {row[2]:.2f}</p>
                            <p class="mb-3"><strong>Calculated Grade:</strong> <span class="badge bg-{badge} fs-6">{grade}</span></p>
                            <div>
                                <a href="updateStudent?id={row[0]}" class="btn btn-sm btn-outline-primary me-2"><i class="bi bi-pencil"></i> Edit</a>
                                <a href="deleteStudent?id={row[0]}" class="btn btn-sm btn-outline-danger" onclick="return confirm('Delete this record?');"><i class="bi bi-trash"></i> Delete</a>
                            </div>
                        </div>'''
                    else:
                        result_html = f'''
                        <div class="alert alert-warning mt-4">
                            <i class="bi bi-exclamation-circle-fill me-2"></i>No student record found with ID <strong>{sid}</strong>.
                        </div>'''
                except ValueError:
                    result_html = '<div class="alert alert-danger mt-4">Please enter a valid numerical ID.</div>'

            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Search Student - Smart Student Management System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body style="background: #f0f2f5;">
    <nav class="navbar navbar-expand-lg navbar-dark" style="background: linear-gradient(135deg, #667eea, #764ba2);">
        <div class="container">
            <a class="navbar-brand fw-bold" href="dashboard.jsp"><i class="bi bi-mortarboard-fill me-2"></i>Student Management</a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link text-white me-3" href="dashboard.jsp">Dashboard</a>
                <a class="nav-link text-white me-3" href="viewStudents">View All</a>
                <a class="nav-link text-white" href="logout">Logout</a>
            </div>
        </div>
    </nav>
    <div class="container my-5" style="max-width: 650px;">
        <div class="card shadow-sm border-0 rounded-4 p-4 bg-white">
            <h3 class="fw-bold mb-3"><i class="bi bi-search text-warning me-2"></i>Search Student by ID</h3>
            <form action="searchStudent" method="GET">
                <div class="input-group mb-3">
                    <input type="number" class="form-control" name="id" placeholder="Enter Student ID (e.g. 1, 2, 3)" required autofocus value="{search_id or ''}">
                    <button class="btn btn-warning text-dark fw-bold" type="submit">Search</button>
                </div>
            </form>
            {result_html}
        </div>
    </div>
</body>
</html>"""
            self.send_html(html)
            return

        # Route: Edit Student Form
        if path in ['/updateStudent', '/editStudent.jsp']:
            sid = query.get('id', [None])[0]
            if not sid:
                self.redirect('/viewStudents')
                return
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, marks FROM students WHERE id = ?", (int(sid),))
            row = cursor.fetchone()
            conn.close()
            if not row:
                self.redirect('/viewStudents')
                return

            with open("WebContent/editStudent.jsp", "r", encoding="utf-8") as f:
                raw = f.read()
            raw = raw.replace('<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>', '')
            raw = raw.replace('''<%
    if (session.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
%>''', '')
            raw = raw.replace('<%= request.getAttribute("id") != null ? request.getAttribute("id") : "" %>', str(row[0]))
            raw = raw.replace('<%= request.getAttribute("name") != null ? request.getAttribute("name") : "" %>', row[1])
            raw = raw.replace('<%= request.getAttribute("marks") != null ? request.getAttribute("marks") : "" %>', str(row[2]))
            self.send_html(raw)
            return

        # Route: Delete Student
        if path in ['/deleteStudent']:
            sid = query.get('id', [None])[0]
            if sid:
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM students WHERE id = ?", (int(sid),))
                conn.commit()
                conn.close()
            self.redirect('/viewStudents')
            return

        self.redirect('/login.jsp')

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        # Action: Login
        if self.path in ['/login', '/login.jsp']:
            user = params.get('username', [''])[0]
            pwd = params.get('password', [''])[0]
            if user == 'admin' and pwd == 'admin123':
                token = "admin_auth_token_998822"
                SESSIONS.add(token)
                self.redirect('/dashboard.jsp', cookie=f'session_admin={token}; Path=/')
            else:
                self.redirect('/login.jsp?error=invalid')
            return

        # Protected operations
        if not self.is_authenticated():
            self.redirect('/login.jsp')
            return

        # Action: Add Student
        if self.path in ['/addStudent', '/addStudentServlet']:
            name = params.get('name', [''])[0].strip()
            marks_str = params.get('marks', ['0'])[0]
            try:
                marks = float(marks_str)
                if name and 0.0 <= marks <= 100.0:
                    conn = sqlite3.connect(DB_FILE)
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
                    conn.commit()
                    conn.close()
                    self.redirect('/viewStudents')
                    return
            except ValueError:
                pass
            self.redirect('/addStudent.jsp')
            return

        # Action: Update Student
        if self.path in ['/updateStudent', '/updateStudentServlet']:
            sid = params.get('id', [''])[0]
            name = params.get('name', [''])[0].strip()
            marks_str = params.get('marks', ['0'])[0]
            try:
                marks = float(marks_str)
                if sid and name and 0.0 <= marks <= 100.0:
                    conn = sqlite3.connect(DB_FILE)
                    cursor = conn.cursor()
                    cursor.execute("UPDATE students SET name = ?, marks = ? WHERE id = ?", (name, marks, int(sid)))
                    conn.commit()
                    conn.close()
                    self.redirect('/viewStudents')
                    return
            except ValueError:
                pass
            self.redirect('/viewStudents')
            return

        self.redirect('/dashboard.jsp')

def run_server():
    init_db()
    server_address = ('127.0.0.1', PORT)
    httpd = socketserver.ThreadingTCPServer(server_address, StudentRequestHandler)
    print(f"============================================================")
    print(f" SMART STUDENT MANAGEMENT SYSTEM IS RUNNING!")
    print(f" URL: http://localhost:{PORT}/login.jsp")
    print(f" Default Login Credentials:")
    print(f"   Username: admin")
    print(f"   Password: admin123")
    print(f"============================================================")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
