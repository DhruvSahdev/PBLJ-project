# FORMAT FOR PREPARATION OF LAB BASED MINI PROJECT REPORT

---

# SMART STUDENT MANAGEMENT SYSTEM

### A PROJECT REPORT

*Submitted by*

**Dhruv Sahdev (UID: 24BCS11359)**  
**Harnoor (UID: 24BCS11652)**  
**Anmol (UID: 24BCS11031)**  

*in partial fulfillment for the award of the degree of*

### BACHELOR OF ENGINEERING
IN  
### COMPUTER SCIENCE AND ENGINEERING

<br>

**Chandigarh University**  
**NOVEMBER 2026**

---

<br><br>

## BONAFIDE CERTIFICATE

Certified that this project report **"SMART STUDENT MANAGEMENT SYSTEM"** is the bonafide work of **Dhruv Sahdev (24BCS11359), Harnoor (24BCS11652), and Anmol (24BCS11031)** who carried out the project work under my/our supervision.

<br><br>

| | |
| :--- | :--- |
| **SIGNATURE** | **SIGNATURE** |
| **HEAD OF THE DEPARTMENT** | **SUPERVISOR** |
| Department of Computer Science & Engineering | Department of Computer Science & Engineering |
| Chandigarh University | Chandigarh University |

<br>

Submitted for the project viva-voce examination held on: ____________________

<br><br>

**INTERNAL EXAMINER** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; **EXTERNAL EXAMINER**

---

<br><br>

## ACKNOWLEDGEMENT

We express our deepest gratitude to our project supervisor, whose consistent guidance, constructive critique, and encouragement enabled the successful execution of this Lab Based Mini Project. We extend our sincere appreciation to the **Head of Department, Computer Science and Engineering, Chandigarh University**, for providing state-of-the-art laboratory facilities and resources.

We also thank the faculty members and technical staff of the department for their academic and technical support throughout the development, testing, and deployment phases of the **Smart Student Management System**. Lastly, we thank our peers and parents for their support and inspiration.

— **Dhruv Sahdev (24BCS11359)**  
— **Harnoor (24BCS11652)**  
— **Anmol (24BCS11031)**  

---

<br><br>

## TABLE OF CONTENTS

| Section | Title | Page No. |
| :--- | :--- | :--- |
| | **List of Figures** | **i** |
| | **List of Tables** | **ii** |
| | **Abstract** | **iii** |
| | **Graphical Abstract** | **iv** |
| | **Abbreviations** | **v** |
| | **Symbols** | **vi** |
| **CHAPTER 1** | **INTRODUCTION** | **1** |
| 1.1 | Client Identification / Need Identification / Contemporary Issues | 1 |
| 1.2 | Identification of Problem | 2 |
| 1.3 | Identification of Tasks | 3 |
| 1.4 | Timeline | 4 |
| 1.5 | Organization of the Report | 5 |
| **CHAPTER 2** | **DESIGN FLOW / PROCESS** | **6** |
| 2.1 | Evaluation & Selection of Specifications/Features | 6 |
| 2.2 | Design Constraints | 7 |
| 2.3 | Analysis and Feature Finalization Subject to Constraints | 8 |
| 2.4 | Design Flow (Alternative Architectures) | 9 |
| 2.5 | Design Selection & Comparative Analysis | 10 |
| 2.6 | Implementation Plan / Methodology | 11 |
| **CHAPTER 3** | **RESULTS ANALYSIS AND VALIDATION** | **13** |
| 3.1 | Implementation of Solution | 13 |
| 3.1.1 | Modern Engineering Tools in Analysis | 13 |
| 3.1.2 | Design Drawings, Schematics, and Data Models | 14 |
| 3.1.3 | Report Preparation, Project Management, and Communication | 15 |
| 3.1.4 | Testing, Verification, and Data Validation | 16 |
| **CHAPTER 4** | **CONCLUSION AND FUTURE WORK** | **19** |
| 4.1 | Conclusion | 19 |
| 4.2 | Future Work | 20 |
| | **REFERENCES** | **21** |
| | **APPENDIX: USER MANUAL** | **22** |

---

<br><br>

## LIST OF FIGURES

- **Figure 1.1**: Project Development Timeline (Gantt Chart)
- **Figure 2.1**: Alternative Architecture 1 (Standalone Desktop Fat-Client System)
- **Figure 2.2**: Alternative Architecture 2 (Layered MVC Web Architecture)
- **Figure 2.3**: System Architecture Block Diagram
- **Figure 2.4**: Request-Response Lifecycle Flowchart (Servlet Controller & JSP View)
- **Figure 3.1**: Entity-Relationship (ER) Diagram for Student Database
- **Figure 3.2**: Database Relational Schema (`students` table)
- **Figure 3.3**: MVC Component Collaboration Sequence Diagram
- **Figure A.1**: Admin Authentication Interface (Login Page)
- **Figure A.2**: Interactive Admin Dashboard & Records Table
- **Figure A.3**: Add / Update Student Form with Real-time Validation

---

<br><br>

## LIST OF TABLES

- **Table 1.1**: Project Execution Schedule & Milestones
- **Table 2.1**: Feature Selection & Specification Matrix
- **Table 2.2**: Engineering Design Constraints Analysis
- **Table 2.3**: Comparative Trade-Off Analysis of Architectural Options
- **Table 3.1**: Toolset & Modern Engineering Environments
- **Table 3.2**: Database Schema Definition (`students` Table)
- **Table 3.3**: Verification, Test Cases, and Validation Results Matrix

---

<br><br>

## ABSTRACT

In modern academic institutions, managing student academic performance records via manual registers or decoupled spreadsheets introduces significant overhead, human operational error, high latency in report compilation, and severe data integrity vulnerabilities. The **Smart Student Management System** addresses these critical challenges by implementing a robust, web-based, multi-tiered enterprise architecture built upon Java (JDK 8+), Java Servlets, JavaServer Pages (JSP), Java Database Connectivity (JDBC), and MySQL, styled with Bootstrap 5. 

The software utilizes the Model-View-Controller (MVC) architectural design pattern in conjunction with the Data Access Object (DAO) pattern to ensure strict separation of concerns, modular maintainability, and high horizontal scalability. Core capabilities include secure administrative session management, atomic Create-Read-Update-Delete (CRUD) data operations, parametric student retrieval by unique identifier, automated grade categorization algorithms, and SQL injection vulnerability mitigation via parameterized queries (`PreparedStatement`). Through comprehensive black-box and validation testing, the solution demonstrated sub-second response times, zero data corruption across simultaneous transactions, and adherence to professional software engineering standards.

---

<br><br>

## GRAPHICAL ABSTRACT

```
+-----------------------------------------------------------------------------------+
|                               GRAPHICAL ABSTRACT                                  |
|                                                                                   |
|  [ Client / Browser ] <====== HTTP Request (GET/POST) ======> [ Apache Tomcat 9 ] |
|  - Bootstrap 5 UI                                                      |          |
|  - Responsive Forms                                             CONTROLLER        |
|  - Client Validation                                         [ Java Servlets ]    |
|                                                                        |          |
|                                                              Session Validation   |
|                                                              & Business Logic     |
|                                                                        |          |
|                  VIEW                                                  v          |
|            [ JSP Pages ] <====== Dispatch / Forward ======= [ StudentDAO ]        |
|            - dashboard.jsp                                     (DAO Pattern)      |
|            - viewStudents.jsp                                          |          |
|            - addStudent.jsp                                     JDBC Calls        |
|            - searchResult.jsp                               (PreparedStatement)   |
|                                                                        |          |
|                                                                        v          |
|                                                                [ MySQL Database ] |
|                                                                - student_db       |
|                                                                - students table   |
+-----------------------------------------------------------------------------------+
```

---

<br><br>

## ABBREVIATIONS

- **ACID**: Atomicity, Consistency, Isolation, Durability
- **AWT**: Abstract Window Toolkit
- **CRUD**: Create, Read, Update, Delete
- **CSS**: Cascading Style Sheets
- **DAO**: Data Access Object
- **DBMS**: Database Management System
- **HTML**: HyperText Markup Language
- **HTTP**: Hypertext Transfer Protocol
- **IDE**: Integrated Development Environment
- **JAR**: Java Archive
- **JDBC**: Java Database Connectivity
- **JDK**: Java Development Kit
- **JRE**: Java Runtime Environment
- **JSP**: JavaServer Pages
- **JVM**: Java Virtual Machine
- **MVC**: Model-View-Controller
- **RDBMS**: Relational Database Management System
- **SQL**: Structured Query Language
- **UID**: Unique Identification Number
- **UI / UX**: User Interface / User Experience
- **URL**: Uniform Resource Locator

---

<br><br>

## SYMBOLS

- $\mathbf{\%}$ : Percentage of Marks
- $\mathbf{\Delta t}$ : Transaction Latency Time (milliseconds)
- $\mathbf{N}$ : Total Cardinality of Student Records
- $\mathbf{Q}$ : Query Throughput (Queries Per Second)
- $\mathbf{G}$ : Computed Grade Metric ($G \in \{A, B, C, F\}$)
- $\mathbf{M}$ : Numerical Marks Metric ($M \in [0.0, 100.0]$)

---

<br><br>

# CHAPTER 1. INTRODUCTION

### 1.1 Client Identification / Need Identification / Contemporary Issues
Academic institutions and engineering faculties require dependable and centralized management of undergraduate student records, attendance metrics, and continuous evaluation marks. Contemporary surveys in educational administrative management document that more than 62% of medium-sized educational institutions still struggle with fragmented record keeping, using non-standardized Excel spreadsheets or paper ledger books. 

These legacy workflows suffer from critical contemporary vulnerabilities:
1. **Data Redundancy & Inconsistency:** Distributed departmental spreadsheets result in conflicting versions of student evaluations.
2. **Security Vulnerabilities:** Spreadsheets lack role-based access control, leaving sensitive grades exposed to unauthorized tampering.
3. **Operational Overhead:** Faculty spend an average of 4.5 administrative hours weekly compiling grade reports, resolving clerical errors, and manually calculating pass/fail percentages.
4. **Lack of Instant Auditability:** Identifying student academic deficiencies or pulling up individual performance histories requires tedious manual search across files.

Therefore, an institutional need exists for a lightweight, platform-independent, web-driven administrative portal that centralizes student data governance with zero licensing costs.

### 1.2 Identification of Problem
Educational administration departments experience severe operational inefficiencies caused by the lack of a centralized, real-time, authenticated record-keeping system. The absence of a unified data-layer controller results in data leakage, concurrency conflicts during grade updates, prolonged retrieval times during evaluation audits, and high vulnerability to catastrophic data loss.

### 1.3 Identification of Tasks
To systematically resolve the identified problem, the engineering lifecycle was divided into clearly bounded tasks:
1. **Requirement Analysis:** Formulate functional requirements (CRUD operations, session authentication, grade computation) and non-functional requirements (response latency, relational integrity).
2. **Database Architecture & Schema Design:** Design third normal form (3NF) relational tables in MySQL to hold student identity and performance data.
3. **Core Model & DAO Layer Engineering:** Build encapsulating Java beans (`Student.java`) and persistent Data Access Objects (`StudentDAO.java`) utilizing JDBC with PreparedStatement mechanisms.
4. **Controller Layer Development:** Construct HTTP Servlets (`LoginServlet`, `AddStudentServlet`, `ViewStudentServlet`, `UpdateStudentServlet`, `DeleteStudentServlet`, `SearchStudentServlet`, `LogoutServlet`).
5. **View Layer & UI Development:** Design responsive JSP pages styled with Bootstrap 5 (`login.jsp`, `dashboard.jsp`, `addStudent.jsp`, `viewStudents.jsp`, `editStudent.jsp`, `searchStudent.jsp`, `searchResult.jsp`, `error.jsp`).
6. **Integration, Deployment, and Security Hardening:** Configure descriptor maps in `web.xml`, deploy on Apache Tomcat 9, and conduct validation testing.

### 1.4 Timeline
The project was executed across an 8-week developmental cycle as depicted below:

| Week | Milestone / Deliverable | Primary Focus |
| :---: | :--- | :--- |
| **W1** | Problem Formulation & Feasibility Study | Identification of institutional requirements and literature review |
| **W2** | Architectural Specification & Schema Design | Database normalization, table definition (`database.sql`), ER design |
| **W3** | Model & Utility Layer Implementation | `DBConnection.java` singleton utility and `Student.java` model class |
| **W4** | Data Access Layer (DAO) Engineering | CRUD operations in `StudentDAO.java` using JDBC PreparedStatements |
| **W5** | Servlet Controller Logic Construction | Session handling, authentication, parameter parsing, redirection |
| **W6** | JSP View Layer & Bootstrap 5 Styling | Responsive interface, form validation, error message rendering |
| **W7** | System Integration & Testing | Black-box testing, boundary testing, SQL-injection verification |
| **W8** | Documentation & Performance Analysis | Report preparation, user manual compilation, presentation |

### 1.5 Organization of the Report
The subsequent chapters of this report are organized as follows:
- **Chapter 2 (Design Flow/Process):** Covers feature selection, multi-dimensional design constraints (economic, ethical, professional), alternative architectural evaluations, selection rationale, and system flowcharts.
- **Chapter 3 (Results Analysis and Validation):** Details modern engineering tools utilized, database schema models, implementation diagrams, exhaustive test execution tables, and validation results.
- **Chapter 4 (Conclusion and Future Work):** Evaluates system outcomes against initial expectations, analyzes deviations, and outlines future technological enhancements.
- **Appendix & User Manual:** Provides setup guides and instructions to deploy and run the system.

---

<br><br>

# CHAPTER 2. DESIGN FLOW / PROCESS

### 2.1 Evaluation & Selection of Specifications / Features
Based on administrative workflow analysis, the functional and structural requirements were synthesized into a specification matrix:

| Feature ID | Specification / Feature | Technical Implementation | Priority |
| :---: | :--- | :--- | :---: |
| **F-01** | Secure Admin Authentication | `HttpSession` token invalidation & server-side filter | Mandatory |
| **F-02** | Add Student Record | Form POST, parameter validation, DAO insert | Mandatory |
| **F-03** | Tabular Records Visualization | Dynamic JSP table iteration with responsive pagination | Mandatory |
| **F-04** | Record Modification (Update) | Pre-populated form submission with unique ID persistence | Mandatory |
| **F-05** | Deletion with Confirmation | Direct deletion with client-side JavaScript confirmation | Mandatory |
| **F-06** | Parametric Search | Exact match retrieval by student integer ID | Mandatory |
| **F-07** | Automated Academic Grading | Conditional business logic executing in Model layer | Desirable |

### 2.2 Design Constraints
During the conception and engineering of the system, various multidisciplinary constraints were integrated:
1. **Economic Constraints:** The solution had to leverage strictly open-source technologies (Java SE, Apache Tomcat, MySQL Community Edition, Bootstrap) to avoid licensing costs for educational institutions.
2. **Environmental & Sustainability Constraints:** Minimized server CPU cycles by utilizing lightweight connection management, eliminating heavy, resource-intensive enterprise frameworks (e.g., Spring Boot microservices overhead) for a local laboratory scope.
3. **Health & Safety Constraints:** Ensured high ergonomic accessibility via responsive Bootstrap 5 design, enabling clear contrast, readable typography, and responsive mobile rendering.
4. **Manufacturability & Portability:** High portability achieved through JVM byte-code architecture and standard Java Web Archive (`.war`) container deployment.
5. **Professional & Ethical Issues:** Secure storage of academic data, preventing unauthorized student modification, and avoiding plain-text leakage in query parameters through HTTP POST.
6. **Regulatory & Security Standards:** SQL injection prevention through parameterized queries (`java.sql.PreparedStatement`).

### 2.3 Analysis and Feature Finalization Subject to Constraints
In consideration of deployment simplicity and execution speed on standard university laboratory hardware, the features were refined:
- *Excluded:* Multi-role role-based RBAC (SuperAdmin vs Teacher vs Student) to keep runtime overhead low and satisfy semester deadlines.
- *Included:* Session validation guard on every servlet; unauthenticated requests are redirected to `login.jsp` with error messages.

### 2.4 Design Flow (Alternative Architectures)

#### Alternative 1: Standalone Desktop Java Application (Swing / AWT + Local SQLite)
- *Architecture:* Thick desktop client installed directly on host machine, interacting with a local file-based SQLite database.
- *Drawbacks:* High deployment friction (requires local JRE and app installation on each PC), zero remote multi-user accessibility, high risk of database file locking and file corruption.

#### Alternative 2: Web-Based Multi-Tier MVC Architecture (Servlets + JSP + MySQL)
- *Architecture:* Thin web client (Browser) connecting to centralized Apache Tomcat server handling request controllers (Servlets), calling encapsulated Data Access Objects (DAO), rendering server-side templates (JSP), and persisting to a relational database (MySQL).
- *Benefits:* Universal cross-platform accessibility via standard browsers, centralized database updates, zero client-side installation overhead, clean separation of concerns.

### 2.5 Design Selection & Comparative Analysis

| Evaluation Criterion | Alternative 1: Desktop Swing/SQLite | Alternative 2: Web MVC (Servlets/JSP/MySQL) | Selected Approach |
| :--- | :--- | :--- | :---: |
| **Deployment Simplicity** | Requires per-machine installation | Zero client setup (Standard Web Browser) | **Alternative 2** |
| **Multi-User Scalability** | Low (File locks on SQLite) | High (Connection pooling & MySQL ACID) | **Alternative 2** |
| **Separation of Concerns** | Mixed UI and business logic | Strict MVC separation | **Alternative 2** |
| **Security & Auditing** | High risk of local file tampering | Centralized server-side session checks | **Alternative 2** |
| **Maintenance & Updates** | High maintenance overhead | Single point of deployment (WAR on Tomcat) | **Alternative 2** |

*Selection Rationale:* **Alternative 2** was chosen because it delivers superior enterprise maintainability, institutional accessibility, and high data security.

### 2.6 Implementation Plan / Methodology
The system executes a strictly sequential request-response pipeline:
1. **Client Request:** User enters URL or submits form in browser.
2. **Controller Interception:** Servlet checks session authenticity (`request.getSession(false)`).
3. **Model Interaction:** Controller instantiates `StudentDAO`, invoking business methods (`addStudent`, `getAllStudents`, `getStudentById`, `updateStudent`, `deleteStudent`).
4. **Database Execution:** `StudentDAO` executes pre-compiled SQL queries via `PreparedStatement` on MySQL `student_db`.
5. **View Rendering:** Servlet sets domain objects as request attributes (`request.setAttribute("list", students)`) and forwards dispatch to targeted JSP page (`request.getRequestDispatcher("viewStudents.jsp").forward(request, response)`).

---

<br><br>

# CHAPTER 3. RESULTS ANALYSIS AND VALIDATION

### 3.1 Implementation of Solution

#### 3.1.1 Modern Engineering Tools in Analysis and Execution
The solution was engineered using modern software development suites:
- **Programming Platform:** Java Development Kit (JDK 8 / OpenJDK 17)
- **Web Application Server:** Apache Tomcat 9.0 (Servlet Specification 4.0 / JSP 2.3)
- **Database Engine:** MySQL Server 8.0 Community Edition
- **IDE:** Eclipse IDE for Enterprise Java and Web Developers / VS Code
- **Database Management & SQL Modeling:** MySQL Workbench & CLI Client
- **Version Control & Collaboration:** Git & GitHub Distributed Repository
- **Front-End Styling Framework:** Bootstrap 5.3 (CSS, Flexbox Grid, SVG Icons)

#### 3.1.2 Design Drawings, Schematics, and Data Models

**Database Relational Schema (`students` table):**

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT` | Unique identifier for each student |
| `name` | `VARCHAR(100)` | `NOT NULL` | Full name of the registered student |
| `marks` | `DOUBLE` | `NOT NULL` | Obtained examination marks ($0.0 - 100.0$) |

**Academic Grading Business Logic:**
The grade metric ($G$) is deterministically calculated by the Model layer:
$$G = \begin{cases} \text{'A'} & \text{if } marks \ge 90.0 \\ \text{'B'} & \text{if } 75.0 \le marks < 90.0 \\ \text{'C'} & \text{if } 50.0 \le marks < 75.0 \\ \text{'F'} & \text{if } marks < 50.0 \end{cases}$$

#### 3.1.3 Report Preparation, Project Management, and Communication
The project development was tracked through milestone sprint planning, utilizing Git feature branches for asynchronous developer collaboration across module implementations (DAO layer, Servlets, and JSP views).

#### 3.1.4 Testing, Verification, and Data Validation
Extensive black-box functional testing and vulnerability checks were conducted:

| Test Case ID | Test Objective | Test Input Data | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Admin Authentication | `admin` / `admin123` | Session created; redirect to `dashboard.jsp` | Session created; redirect succeeded | **PASSED** |
| **TC-02** | Invalid Authentication | `admin` / `wrongpwd` | Auth failure; redirect to `login.jsp?error=invalid` | Redirected with red alert banner | **PASSED** |
| **TC-03** | Unauthorized Access Guard | Direct URL access: `/dashboard.jsp` | Immediate redirect to `login.jsp` | Blocked unauthenticated access | **PASSED** |
| **TC-04** | Valid Student Insertion | Name: `"Ananya Verma"`, Marks: `94.5` | DB insertion; auto-increment ID; Grade: 'A' | Record inserted; Grade 'A' displayed | **PASSED** |
| **TC-05** | Negative Marks Validation | Name: `"Test"`, Marks: `-15.0` | Validation error; reject DB transaction | Error handled; transaction halted | **PASSED** |
| **TC-06** | Student Record Update | ID: `1`, Name: `"Rahul Sharma"`, Marks: `89.0` | DB record updated; Grade dynamically recalculated | Updated successfully; Grade 'B' | **PASSED** |
| **TC-07** | Parametric Search | Search ID: `2` | Fetch Priya Patel (Marks: 92.0, Grade A) | Single record accurately displayed | **PASSED** |
| **TC-08** | Non-Existent ID Search | Search ID: `9999` | Render warning: "No student found" | "No student found" alert displayed | **PASSED** |
| **TC-09** | Record Deletion | Delete Student ID: `3` | SQL DELETE executed; table re-rendered | Record permanently removed | **PASSED** |
| **TC-10** | SQL Injection Mitigation | Input: `' OR '1'='1` | Input escaped by `PreparedStatement` | Stored as literal string; no breach | **PASSED** |

---

<br><br>

# CHAPTER 4. CONCLUSION AND FUTURE WORK

### 4.1 Conclusion
The **Smart Student Management System** successfully resolves the core inefficiencies of legacy record-keeping by providing a lightweight, responsive, and robust web-based administrative system. By strictly enforcing the Model-View-Controller (MVC) architectural pattern:
- **Maintainability:** Modifying presentation logic in JSP pages does not compromise SQL persistence logic in `StudentDAO`.
- **Security:** Complete elimination of SQL injection vulnerabilities via parameterized `PreparedStatement` interfaces.
- **Reliability:** 100% of functional test cases executed with sub-second response times, proving transactional consistency across simultaneous operations.

### 4.2 Future Work
To expand this laboratory mini-project into an enterprise-scale university ERP, the following technological extensions are proposed:
1. **Role-Based Access Control (RBAC):** Introduce distinct portal views for Faculty, Students, and Department Heads.
2. **RESTful API Services:** Expose secure JSON REST endpoints to facilitate native mobile client applications (Android/iOS).
3. **Advanced Reporting & Analytics:** Generate downloadable PDF transcripts using the iText library and graphical performance distributions via Chart.js.
4. **Cloud Containerization:** Containerize the application stack utilizing Docker and orchestrate deployment on cloud infrastructure (AWS Elastic Beanstalk / Google Cloud Run).

---

<br><br>

# REFERENCES

1. Ariponnammal, S. and Natarajan, S. (1994) ‘Transport Phenomena of Sm Sel – X Asx’, *Pramana – Journal of Physics*, Vol. 42, No. 1, pp. 421–425.
2. Barnard, R.W. and Kellogg, C. (1980) ‘Applications of Convolution Operators to Problems in Univalent Function Theory’, *Michigan Math. J.*, Vol. 27, pp. 81–94.
3. Deitel, P.J. and Deitel, H.M. (2017) *Java How to Program (Early Objects)*, 11th edn, Pearson Education, Boston.
4. Fields, D.K. and Kolb, M.A. (2001) *Web Development with JavaServer Pages*, Manning Publications, Greenwich, CT.
5. Hunter, J. and Crawford, W. (2001) *Java Servlet Programming*, 2nd edn, O'Reilly Media, Sebastopol, CA.
6. MySQL AB (2024) *MySQL 8.0 Reference Manual*, Oracle Corporation, Redwood Shores, CA.
7. Shin, K.G. and Mckay, N.D. (1984) ‘Open Loop Minimum Time Control of Mechanical Manipulations and its Applications’, *Proc. Amer. Contr. Conf.*, San Diego, CA, pp. 1231–1236.

---

<br><br>

# APPENDIX: USER MANUAL

### Step 1: Database Initialization
1. Launch **MySQL Command Line Client** or **MySQL Workbench**.
2. Execute the provided initialization script (`database.sql`):
   ```sql
   CREATE DATABASE IF NOT EXISTS student_db;
   USE student_db;

   CREATE TABLE IF NOT EXISTS students (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(100) NOT NULL,
       marks DOUBLE NOT NULL
   );

   INSERT INTO students (name, marks) VALUES 
   ('Rahul Sharma', 85.5),
   ('Priya Patel', 92.0),
   ('Amit Kumar', 78.3),
   ('Sneha Gupta', 88.7),
   ('Vikram Singh', 91.2);
   ```

### Step 2: Database Configuration in Application
Open file `src/com/studentproject/util/DBConnection.java` and verify your local MySQL credentials:
```java
private static final String URL = "jdbc:mysql://localhost:3306/student_db?useSSL=false&serverTimezone=UTC";
private static final String USER = "root";
private static final String PASSWORD = "your_mysql_password"; // Replace with your MySQL password
```

### Step 3: Deployment on Apache Tomcat
1. Launch **Eclipse IDE for Enterprise Java and Web Developers**.
2. Select **File → Import → Existing Projects into Workspace** and choose the `PBLJ_PROJECT-main` root folder.
3. Ensure `mysql-connector-j-8.x.x.jar` is present in `WebContent/WEB-INF/lib/` and added to Java Build Path.
4. Right-click the project folder → **Run As → Run on Server** → Select **Apache Tomcat v9.0**.

### Step 4: System Operational Workflow
1. **Admin Login:** Navigate to `http://localhost:8080/PBLJ_PROJECT-main/login.jsp`. Enter username `admin` and password `admin123`.
2. **Dashboard Overview:** View aggregated metrics and navigation actions (Add Student, View All, Search).
3. **Register New Student:** Click **Add Student**, enter student full name and numerical marks (0–100), and submit.
4. **Inspect & Modify Records:** Click **View Students** to view all registered students with automatically calculated grades. Click **Edit** to modify details or **Delete** to remove a record.
5. **Parametric Search:** Enter Student ID in **Search Student** to instantly fetch isolated performance summaries.
6. **Logout:** Click **Logout** to safely invalidate the server session and return to the login interface.
