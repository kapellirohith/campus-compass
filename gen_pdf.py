import os

# Try to install fpdf2 silently if not already installed
os.system('pip install fpdf2 > /dev/null 2>&1')

from fpdf import FPDF

class PDF(FPDF):
    def add_hero(self):
        try:
            # Add hero image taking up full width at top, mimicking a high-impact website header
            self.image('images/hero.jpg', x=0, y=0, w=210, h=70)
        except Exception:
            pass
            
        self.set_y(85)
        # Title Hierarchy mimicking the website
        self.set_font('times', 'B', 34)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 12, 'CAMPUS COMPASS', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.set_font('times', 'I', 14)
        self.set_text_color(90, 100, 116) # Muted Navy
        self.cell(0, 8, 'The Unofficial Amrita Amaravati Handbook', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.ln(6)
        self.set_font('helvetica', 'B', 11)
        self.set_text_color(185, 28, 28) # Amrita Red
        self.cell(0, 8, 'FRESHERS SURVIVAL SHEET', align='C', new_x='LMARGIN', new_y='NEXT')
        
        # Subtle divider
        self.ln(10)
        self.set_draw_color(229, 231, 235)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(10)

    def section_title(self, title):
        self.ln(8)
        self.set_font('times', 'B', 16) # Using Times to simulate Instrument Serif
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 8, title, align='L', new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)

    def add_bullet(self, text):
        self.set_font('helvetica', '', 11)
        self.set_text_color(15, 27, 45)
        self.cell(0, 7, f"-  {text}", new_x='LMARGIN', new_y='NEXT')
        
    def add_check(self, text):
        self.set_font('helvetica', '', 11)
        self.set_text_color(90, 100, 116)
        self.cell(0, 7, f"[   ]  {text}", new_x='LMARGIN', new_y='NEXT')

    def add_text(self, text):
        self.set_font('helvetica', '', 11)
        self.set_text_color(15, 27, 45)
        self.multi_cell(0, 7, text, new_x='LMARGIN', new_y='NEXT')

    def draw_divider(self):
        self.ln(6)
        self.set_draw_color(229, 231, 235)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(6)

pdf = PDF()
# Generous editorial margins
pdf.set_margins(20, 20, 20)
pdf.add_page()
pdf.add_hero()

# SECTION 1
pdf.section_title('Before You Arrive')
pdf.add_check('Admission Letter')
pdf.add_check('Aadhaar Copies')
pdf.add_check('Passport Photos')
pdf.add_check('Laptop + Charger')
pdf.add_check('Medical Documents')

# SECTION 2
pdf.section_title('Rules Nobody Explains')
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(185, 28, 28) # Red Warning
pdf.cell(0, 7, 'Attendance below 75% = FA', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('helvetica', '', 11)
pdf.set_text_color(15, 27, 45)
pdf.multi_cell(0, 7, 'Do not gamble with attendance.', new_x='LMARGIN', new_y='NEXT')

# SECTION 3
pdf.section_title('Digital Lifelines')
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(15, 27, 45)
pdf.cell(20, 7, 'AUMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 11)
pdf.cell(0, 7, 'Academics, Attendance, Grades.', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('helvetica', 'B', 11)
pdf.cell(20, 7, 'GPMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 11)
pdf.cell(0, 7, 'Hostel and Campus Services.', new_x='LMARGIN', new_y='NEXT')

# SECTION 4
pdf.section_title('First Month Checklist')
pdf.add_check('Join one club.')
pdf.add_check('Attend induction events.')
pdf.add_check('Learn AUMS.')
pdf.add_check('Locate classrooms.')
pdf.add_check('Make friends outside your branch.')

pdf.add_page()

# SECTION 5
pdf.section_title('Clubs Worth Exploring')
pdf.add_bullet('Chakravyuha')
pdf.add_bullet('ACM')
pdf.add_bullet('IEEE')
pdf.add_bullet('Team bi0s')
pdf.add_bullet('AYUDH')
pdf.add_bullet('E-Cell')

# SECTION 6 - FIVE THINGS TO REMEMBER (Visually Dominant)
pdf.ln(15)
pdf.set_font('times', 'B', 22)
pdf.set_text_color(15, 27, 45)
pdf.cell(0, 10, 'Five Things To Remember', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.draw_divider()

items = [
    'Attendance below 75% is dangerous.',
    'Join clubs early.',
    'Build projects from Semester 1.',
    'Protect CGPA early.',
    'Make friends outside your branch.'
]
for i, item in enumerate(items, 1):
    # Large subtle numbering
    pdf.set_font('times', 'B', 18)
    pdf.set_text_color(203, 213, 225) # Slate 300
    pdf.cell(12, 8, f"0{i}", new_x='RIGHT')
    # Bold Navy Text
    pdf.set_font('helvetica', 'B', 11)
    pdf.set_text_color(15, 27, 45)
    pdf.cell(0, 8, item, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

pdf.draw_divider()

# SECTION 7
pdf.section_title('Senior Advice')
pdf.add_text('Do not wait until second year to start building.')
pdf.add_text('The students who start in Semester 1 gain an enormous advantage.')

# CLOSING SECTION (Emergency + Quote Unified)
# Pushing this block down to act as a definitive footer
pdf.ln(20)

# Red Emergency
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(185, 28, 28)
pdf.cell(0, 7, 'EMERGENCY REMINDER:', align='C', new_x='LMARGIN', new_y='NEXT')
# Subtle Navy Text
pdf.set_font('helvetica', '', 11)
pdf.set_text_color(15, 27, 45)
pdf.cell(0, 7, 'Screenshot this sheet. Keep a copy on your phone.', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.ln(18)
# Grand Serif Closing Quote
pdf.set_font('times', 'I', 20)
pdf.set_text_color(90, 100, 116)
pdf.multi_cell(0, 10, '"One day you\'ll know every shortcut on campus.\nUntil then, keep this sheet."', align='C', new_x='LMARGIN', new_y='NEXT')

pdf.output('survival-sheet.pdf')
