import os

# Try to install fpdf2 silently if not already installed
os.system('pip install fpdf2 > /dev/null 2>&1')

from fpdf import FPDF

class PDF(FPDF):
    def add_hero(self):
        try:
            # Add hero image taking up full width at top, slimmer height to save space
            self.image('images/hero.jpg', x=0, y=0, w=210, h=45)
        except Exception:
            pass
            
        self.set_y(52)
        # Title Hierarchy mimicking the website
        self.set_font('times', 'B', 28)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 10, 'CAMPUS COMPASS', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.set_font('times', 'I', 12)
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

    def draw_divider(self):
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
pdf.set_font('times', 'B', 14)
pdf.cell(90, 7, 'BEFORE YOU ARRIVE', new_x='LMARGIN', new_y='NEXT')
items = ['Admission Letter', 'Aadhaar Copies', 'Passport Photos', 'Laptop + Charger', 'Medical Documents']
for i in items:
    pdf.set_x(15)
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_text_color(185, 28, 28)
    pdf.cell(5, 5, "[x]", new_x='RIGHT') 
    pdf.set_font('helvetica', '', 10)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(85, 5, i, new_x='LMARGIN', new_y='NEXT')

# RIGHT COL: DIGITAL LIFELINES
pdf.set_y(y_before_cols)
pdf.set_x(110)
pdf.set_font('times', 'B', 14)
pdf.cell(90, 7, 'DIGITAL LIFELINES', new_x='LMARGIN', new_y='NEXT')

lifelines = [
    ('AUMS', 'Attendance, grades, academics.'),
    ('GPMS', 'Hostel and campus services.')
]
for title, desc in lifelines:
    pdf.set_x(110)
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(15, 5, title, new_x='RIGHT')
    pdf.set_font('helvetica', '', 9.5)
    pdf.cell(75, 5, desc, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

pdf.ln(3)
pdf.draw_divider()

# ==========================================
# SECTION 2: FIVE THINGS (Visually Dominant)
# ==========================================
pdf.ln(2)
pdf.set_font('times', 'B', 18)
pdf.set_text_color(15, 27, 45)
pdf.cell(0, 8, 'The Five Things Every Senior Repeats', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

five_things = [
    'Attendance below 75% is dangerous.',
    'Join clubs during your first month.',
    'Start projects in Semester 1.',
    'Protect CGPA early.',
    'Build friendships outside your branch.'
]
for i, item in enumerate(five_things, 1):
    pdf.set_font('times', 'B', 14)
    pdf.set_text_color(185, 28, 28) # Red numbers for punch
    pdf.cell(8, 6, f"{i}.", new_x='RIGHT')
    pdf.set_font('helvetica', 'B', 10.5)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(0, 6, item, new_x='LMARGIN', new_y='NEXT')

pdf.draw_divider()

# ==========================================
# 2-COLUMN LAYOUT: FIRST 30 DAYS & CLUBS
# ==========================================
y_before_cols2 = pdf.get_y()

# LEFT COL: 30 DAYS
pdf.set_x(15)
pdf.set_font('times', 'B', 14)
pdf.cell(90, 7, 'FIRST 30 DAYS', new_x='LMARGIN', new_y='NEXT')

days = [
    ('Week 1', 'Everything feels unfamiliar.'),
    ('Week 2', 'You start recognizing faces.'),
    ('Week 3', 'Classes become routine.'),
    ('Week 4', 'Campus starts feeling like home.')
]
for w, d in days:
    pdf.set_x(15)
    pdf.set_font('helvetica', 'B', 9.5)
    pdf.cell(90, 4.5, w, new_x='LMARGIN', new_y='NEXT')
    pdf.set_x(15)
    pdf.set_font('helvetica', 'I', 9.5)
    pdf.set_text_color(90, 100, 116)
    pdf.cell(90, 4.5, d, new_x='LMARGIN', new_y='NEXT')
    pdf.set_text_color(15, 27, 45)
    pdf.ln(1)

# RIGHT COL: CLUBS
pdf.set_y(y_before_cols2)
pdf.set_x(110)
pdf.set_font('times', 'B', 14)
pdf.cell(90, 7, 'CLUBS WORTH YOUR TIME', new_x='LMARGIN', new_y='NEXT')

clubs = [
    ('Chakravyuha', 'Fastest route into projects and hackathons.'),
    ('ACM', 'Build stronger CS fundamentals.'),
    ('IEEE', 'Engineering and research exposure.'),
    ('Team bi0s', 'Cybersecurity and CTFs.'),
    ('AYUDH', 'Leadership and service.'),
    ('E-Cell', 'Entrepreneurship and startups.')
]
for c, d in clubs:
    pdf.set_x(110)
    pdf.set_font('helvetica', 'B', 9.5)
    pdf.cell(90, 4.5, c, new_x='LMARGIN', new_y='NEXT')
    pdf.set_x(110)
    pdf.set_font('helvetica', '', 9.5)
    pdf.set_text_color(90, 100, 116)
    pdf.cell(90, 4.5, d, new_x='LMARGIN', new_y='NEXT')
    pdf.set_text_color(15, 27, 45)

pdf.ln(1)
pdf.draw_divider()

# ==========================================
# SECTION 6: THE HARD WAY
# ==========================================
pdf.ln(1)
pdf.set_font('times', 'B', 14)
pdf.cell(0, 7, 'THINGS WE LEARNED THE HARD WAY', new_x='LMARGIN', new_y='NEXT')

lessons = [
    ('"I\'ll watch the lecture recording later."', 'You probably won\'t. Attend class.'),
    ('"I\'ll join clubs next semester."', 'Most people never do. Join now.'),
    ('"I\'ll start projects after first year."', 'The students who grow fastest start immediately.')
]
for q, a in lessons:
    pdf.ln(1.5)
    pdf.set_font('helvetica', 'I', 10.5)
    pdf.set_text_color(185, 28, 28)
    pdf.cell(0, 5, q, new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('helvetica', 'B', 10)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(0, 5, a, new_x='LMARGIN', new_y='NEXT')

# ==========================================
# CLOSING SECTION: ONE LAST THING
# ==========================================
# Force this to a visually distinct bottom area
pdf.ln(6)
pdf.set_font('times', 'B', 18)
pdf.cell(0, 8, 'ONE LAST THING', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.ln(2)
pdf.set_font('times', 'I', 13.5)
pdf.set_text_color(90, 100, 116)
ending_text = "One day you'll know every shortcut on campus.\nYou'll know where your classroom is. You'll know where your friends sit during lunch.\nYou'll stop feeling like a visitor.\n\nYou belong here.\nSee you on campus."
pdf.multi_cell(0, 6, ending_text, align='C', new_x='LMARGIN', new_y='NEXT')

pdf.output('survival-sheet.pdf')
