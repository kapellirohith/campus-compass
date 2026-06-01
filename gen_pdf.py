import os

# Try to install fpdf2 silently if not already installed
os.system('pip install fpdf2 > /dev/null 2>&1')

from fpdf import FPDF

class PDF(FPDF):
    def add_hero(self):
        try:
            # Add hero image taking up full width at top, slimmer height
            self.image('images/hero.jpg', x=0, y=0, w=210, h=40)
        except Exception:
            pass
            
        self.set_y(45)
        # Title Hierarchy mimicking the website
        self.set_font('times', 'B', 32)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 10, 'CAMPUS COMPASS', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.set_font('times', 'I', 13)
        self.set_text_color(90, 100, 116) # Muted Navy
        self.cell(0, 6, 'The Unofficial Amrita Amaravati Handbook', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.ln(2)
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(185, 28, 28) # Amrita Red
        self.cell(0, 6, 'FRESHERS SURVIVAL SHEET', align='C', new_x='LMARGIN', new_y='NEXT')
        
        # Subtle divider
        self.ln(4)
        self.set_draw_color(229, 231, 235)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)

pdf = PDF()
# Tight margins to fit 1 page comfortably
pdf.set_margins(15, 15, 15)
pdf.add_page()
pdf.add_hero()

# ==========================================
# 2-COLUMN LAYOUT: BEFORE YOU ARRIVE & DIGITAL LIFELINES
# ==========================================
y_before_cols = pdf.get_y()

# LEFT COL: BEFORE YOU ARRIVE
pdf.set_x(15)
pdf.set_font('times', 'B', 12)
pdf.set_text_color(15, 27, 45)
pdf.cell(90, 6, 'BEFORE YOU ARRIVE', new_x='LMARGIN', new_y='NEXT')
items = ['Admission Letter', 'Aadhaar Copies', 'Passport Photos', 'Laptop + Charger', 'Medical Documents']
for i in items:
    pdf.set_x(15)
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(6, 5, "[   ]", new_x='RIGHT') 
    pdf.set_font('helvetica', '', 9.5)
    pdf.cell(84, 5, i, new_x='LMARGIN', new_y='NEXT')

# RIGHT COL: DIGITAL LIFELINES
pdf.set_y(y_before_cols)
pdf.set_x(110)
pdf.set_font('times', 'B', 12)
pdf.set_text_color(15, 27, 45)
pdf.cell(90, 6, 'DIGITAL LIFELINES', new_x='LMARGIN', new_y='NEXT')

lifelines = [
    ('AUMS', 'Attendance, grades, academics.'),
    ('GPMS', 'Hostel and campus services.')
]
for title, desc in lifelines:
    pdf.set_x(110)
    pdf.set_font('helvetica', 'B', 9.5)
    pdf.cell(15, 5, title, new_x='RIGHT')
    pdf.set_font('helvetica', '', 9)
    pdf.cell(75, 5, desc, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

pdf.ln(5)

# ==========================================
# CALLOUT BOX 1: FIVE THINGS
# ==========================================
box_y = pdf.get_y()
pdf.set_fill_color(249, 250, 251) # Off-white background
pdf.set_draw_color(15, 27, 45) # Navy border
pdf.rect(15, box_y, 180, 58, 'DF') # Draw Filled Rectangle with border

pdf.set_y(box_y + 5)
pdf.set_font('times', 'B', 16)
pdf.set_text_color(15, 27, 45)
pdf.cell(0, 8, 'IF YOU REMEMBER ONLY FIVE THINGS', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.ln(2)
five_things = [
    'Attendance below 75% is dangerous.',
    'Join clubs during induction month.',
    'Start projects in Semester 1.',
    'Protect CGPA early.',
    'Build friendships outside your branch.'
]
for i, item in enumerate(five_things, 1):
    pdf.set_x(25)
    pdf.set_font('times', 'B', 18)
    pdf.set_text_color(185, 28, 28) # Red numbers for punch
    pdf.cell(8, 7, f"{i}", new_x='RIGHT')
    pdf.set_font('helvetica', 'B', 11.5)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(0, 7, item, new_x='LMARGIN', new_y='NEXT')

pdf.set_y(box_y + 64)

# ==========================================
# CALLOUT BOX 2: SENIOR WARNING
# ==========================================
box2_y = pdf.get_y()
pdf.set_fill_color(255, 241, 242) # Very light red background
pdf.set_draw_color(185, 28, 28) # Red border
pdf.rect(15, box2_y, 180, 58, 'DF')

pdf.set_y(box2_y + 5)
pdf.set_font('times', 'B', 15)
pdf.set_text_color(185, 28, 28)
pdf.cell(0, 8, 'MOST COMMON FRESHER MISTAKES', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.ln(1)
lessons = [
    ('"I\'ll start projects later."', 'The students who grow fastest start immediately.'),
    ('"I\'ll join clubs next semester."', 'Most people never do. Join now.'),
    ('"I\'ll study before exams."', 'These decisions create problems later. Start early.')
]
for q, a in lessons:
    pdf.set_x(25)
    pdf.set_font('times', 'I', 13)
    pdf.set_text_color(185, 28, 28)
    pdf.cell(0, 6, q, new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_x(25)
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(0, 5, a, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

pdf.set_y(box2_y + 64)

# ==========================================
# CLOSING SECTION: PREMIUM FOOTER
# ==========================================
box3_y = pdf.get_y()
pdf.set_fill_color(15, 27, 45) # Solid Navy background
pdf.rect(15, box3_y, 180, 45, 'F') # No border, just fill

pdf.set_y(box3_y + 12)
pdf.set_font('times', 'I', 16)
pdf.set_text_color(229, 231, 235)
ending_text = "One day you'll know every shortcut on campus.\nUntil then, keep this sheet."
pdf.multi_cell(0, 7, ending_text, align='C', new_x='LMARGIN', new_y='NEXT')

pdf.ln(5)
pdf.set_font('helvetica', 'B', 12)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 6, 'You belong here. See you on campus.', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.output('survival-sheet.pdf')
