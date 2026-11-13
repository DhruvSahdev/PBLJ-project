from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size, bold=False):
    # Try system fonts on Windows
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf" if not bold else "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arial.ttf" if not bold else "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibri.ttf" if not bold else "C:/Windows/Fonts/calibrib.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_browser_chrome(draw, width, height, title, url):
    # Window Header / Title Bar
    draw.rectangle([0, 0, width, 42], fill="#EAECEF")
    
    # Window controls (mac/windows style dots)
    draw.ellipse([14, 15, 26, 27], fill="#FF5F56")
    draw.ellipse([34, 15, 46, 27], fill="#FFBD2E")
    draw.ellipse([54, 15, 66, 27], fill="#27C93F")
    
    # Active Tab
    draw.rounded_rectangle([80, 8, 300, 42], radius=6, fill="#FFFFFF")
    font_tab = get_font(12, bold=False)
    draw.text((100, 16), title[:28] + "...", fill="#333333", font=font_tab)
    
    # Navigation Bar
    draw.rectangle([0, 42, width, 84], fill="#FFFFFF")
    draw.line([0, 84, width, 84], fill="#E0E0E0", width=1)
    
    # Nav buttons (Back, Forward, Refresh)
    font_nav = get_font(15, bold=True)
    draw.text((20, 52), "←   →   ⟳", fill="#757575", font=font_nav)
    
    # Address Bar
    draw.rounded_rectangle([110, 49, width - 60, 77], radius=14, fill="#F1F3F4")
    font_url = get_font(12, bold=False)
    draw.text((130, 56), "🔒 " + url, fill="#202124", font=font_url)

def create_homepage_screenshot(filename="homepage_screenshot.png"):
    w, h = 1200, 750
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw Browser Frame
    draw_browser_chrome(draw, w, h, "Login - Smart Student Management System", "http://localhost:8080/PBLJ_PROJECT/login.jsp")
    
    # Page Content Area (from y=85 to y=h)
    # Background Linear Gradient (#667eea to #764ba2)
    c1 = (102, 126, 234) # #667eea
    c2 = (118, 75, 162)  # #764ba2
    for y in range(85, h):
        ratio = (y - 85) / (h - 85)
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        draw.line([0, y, w, y], fill=(r, g, b, 255))
        
    # Login Card
    card_w, card_h = 440, 480
    cx1 = (w - card_w) // 2
    cy1 = 85 + (h - 85 - card_h) // 2
    cx2 = cx1 + card_w
    cy2 = cy1 + card_h
    
    # Drop shadow
    for i in range(15):
        alpha = int(30 * (1 - i / 15))
        draw.rounded_rectangle([cx1 - i, cy1 - i, cx2 + i, cy2 + i], radius=24, fill=(0, 0, 0, alpha))
        
    # Card Body
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=20, fill=(255, 255, 255, 250))
    
    # Icon circle
    draw.ellipse([cx1 + card_w//2 - 32, cy1 + 30, cx1 + card_w//2 + 32, cy1 + 94], fill="#EEF2FF")
    font_icon = get_font(32, bold=True)
    draw.text((cx1 + card_w//2 - 18, cy1 + 42), "🎓", font=font_icon, fill="#667eea")
    
    # Title
    font_title = get_font(24, bold=True)
    title_text = "Admin Login"
    draw.text((cx1 + card_w//2 - 68, cy1 + 105), title_text, fill="#2D3748", font=font_title)
    
    # Subtitle
    font_sub = get_font(13, bold=False)
    sub_text = "Smart Student Management System"
    draw.text((cx1 + card_w//2 - 105, cy1 + 140), sub_text, fill="#718096", font=font_sub)
    
    # Input 1: Username
    draw.rounded_rectangle([cx1 + 40, cy1 + 180, cx2 - 40, cy1 + 225], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=2)
    font_in = get_font(13, bold=False)
    draw.text((cx1 + 55, cy1 + 193), "👤   admin", fill="#2D3748", font=font_in)
    
    # Input 2: Password
    draw.rounded_rectangle([cx1 + 40, cy1 + 245, cx2 - 40, cy1 + 290], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=2)
    draw.text((cx1 + 55, cy1 + 258), "🔒   ••••••••", fill="#2D3748", font=font_in)
    
    # Login Button (Gradient)
    bx1, by1, bx2, by2 = cx1 + 40, cy1 + 315, cx2 - 40, cy1 + 365
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=10, fill="#667eea")
    font_btn = get_font(15, bold=True)
    draw.text((cx1 + card_w//2 - 42, cy1 + 327), "➔  Login", fill="#FFFFFF", font=font_btn)
    
    # Credentials Box
    draw.rounded_rectangle([cx1 + 40, cy1 + 395, cx2 - 40, cy1 + 445], radius=10, fill="#F8FAFC", outline="#E2E8F0", width=1)
    font_info = get_font(12, bold=False)
    draw.text((cx1 + 65, cy1 + 405), "ℹ️ Default Credentials:", fill="#64748B", font=font_info)
    font_cred = get_font(12, bold=True)
    draw.text((cx1 + 65, cy1 + 423), "Username: admin   |   Password: admin123", fill="#334155", font=font_cred)
    
    img.convert("RGB").save(filename, "PNG")
    print(f"Created {filename}")

def create_dashboard_screenshot(filename="dashboard_screenshot.png"):
    w, h = 1200, 750
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw Browser Frame
    draw_browser_chrome(draw, w, h, "Dashboard - Smart Student Management System", "http://localhost:8080/PBLJ_PROJECT/dashboard.jsp")
    
    # Content Area background
    draw.rectangle([0, 85, w, h], fill="#F8FAFC")
    
    # Navbar
    draw.rectangle([0, 85, w, 145], fill="#667eea")
    font_brand = get_font(17, bold=True)
    draw.text((40, 102), "🎓  Smart Student Management System", fill="#FFFFFF", font=font_brand)
    
    font_user = get_font(13, bold=False)
    draw.text((w - 240, 106), "Welcome, Admin  |  🚪 Logout", fill="#FFFFFF", font=font_user)
    
    # Hero Banner
    draw.rounded_rectangle([40, 165, w - 40, 245], radius=15, fill="#764ba2")
    font_hero1 = get_font(20, bold=True)
    draw.text((65, 182), "Welcome to Administration Dashboard", fill="#FFFFFF", font=font_hero1)
    font_hero2 = get_font(13, bold=False)
    draw.text((65, 214), "Manage student academic records, continuous evaluations, and grade reports securely.", fill="#E2E8F0", font=font_hero2)
    
    # 3 Action Cards
    card_configs = [
        ("➕ Add Student", "Register new student with evaluation marks", "#2563EB", 40),
        ("📋 View All Students", "Browse all enrolled student records & grades", "#16A34A", 420),
        ("🔍 Search Student", "Locate individual student records by unique ID", "#D97706", 800)
    ]
    
    for title, desc, col, x in card_configs:
        draw.rounded_rectangle([x, 265, x + 360, 395], radius=12, fill="#FFFFFF", outline="#E2E8F0", width=1)
        draw.ellipse([x + 20, 285, x + 65, 330], fill=col)
        font_c_title = get_font(16, bold=True)
        draw.text((x + 80, 295), title, fill="#1E293B", font=font_c_title)
        font_c_desc = get_font(12, bold=False)
        draw.text((x + 20, 345), desc, fill="#64748B", font=font_c_desc)
    
    # Records Preview Table Header
    draw.text((40, 420), "Student Performance Records (Sample Overview)", fill="#1E293B", font=get_font(16, bold=True))
    
    # Table Box
    tx1, ty1, tx2, ty2 = 40, 450, w - 40, 710
    draw.rounded_rectangle([tx1, ty1, tx2, ty2], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=1)
    
    # Table Head
    draw.rectangle([tx1, ty1, tx2, ty1 + 40], fill="#F1F5F9")
    font_th = get_font(13, bold=True)
    draw.text((60, ty1 + 12), "ID", fill="#475569", font=font_th)
    draw.text((150, ty1 + 12), "Student Name", fill="#475569", font=font_th)
    draw.text((450, ty1 + 12), "Evaluation Marks", fill="#475569", font=font_th)
    draw.text((680, ty1 + 12), "Grade", fill="#475569", font=font_th)
    draw.text((880, ty1 + 12), "Actions", fill="#475569", font=font_th)
    
    # Rows
    rows = [
        ("1", "Rahul Sharma", "85.5 %", "Grade B", "#2563EB"),
        ("2", "Priya Patel", "92.0 %", "Grade A", "#16A34A"),
        ("3", "Amit Kumar", "78.3 %", "Grade B", "#2563EB"),
        ("4", "Sneha Gupta", "88.7 %", "Grade B", "#2563EB"),
        ("5", "Vikram Singh", "91.2 %", "Grade A", "#16A34A"),
    ]
    
    font_td = get_font(13, bold=False)
    font_badge = get_font(11, bold=True)
    
    curr_y = ty1 + 45
    for rid, name, marks, grade, bcol in rows:
        draw.line([tx1, curr_y - 5, tx2, curr_y - 5], fill="#F1F5F9", width=1)
        draw.text((60, curr_y + 8), rid, fill="#1E293B", font=font_td)
        draw.text((150, curr_y + 8), name, fill="#1E293B", font=font_td)
        draw.text((450, curr_y + 8), marks, fill="#1E293B", font=font_td)
        
        # Badge
        draw.rounded_rectangle([680, curr_y + 5, 755, curr_y + 27], radius=6, fill=bcol)
        draw.text((690, curr_y + 8), grade, fill="#FFFFFF", font=font_badge)
        
        # Buttons
        draw.rounded_rectangle([880, curr_y + 5, 935, curr_y + 27], radius=5, fill="#3B82F6")
        draw.text((890, curr_y + 8), "Edit", fill="#FFFFFF", font=font_badge)
        
        draw.rounded_rectangle([945, curr_y + 5, 1010, curr_y + 27], radius=5, fill="#EF4444")
        draw.text((955, curr_y + 8), "Delete", fill="#FFFFFF", font=font_badge)
        
        curr_y += 42
        
    img.convert("RGB").save(filename, "PNG")
    print(f"Created {filename}")

if __name__ == "__main__":
    create_homepage_screenshot()
    create_dashboard_screenshot()
