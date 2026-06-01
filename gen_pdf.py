import os

# Try to install fpdf2 silently if not already installed
os.system('pip install fpdf2 > /dev/null 2>&1')

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # We will manually place the header items since we have an image
        pass

    def add_hero(self):
        try:
            self.image('images/hero.jpg', x=0, y=0, w=210, h=60) # A4 is 210mm wide
        except Exception:
            pass # fallback if image doesn't exist
            
        self.set_y(65)
        self.set_font('helvetica', 'B', 24)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 10, 'CAMPUS COMPASS', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('helvetica', 'I', 12)
        self.cell(0, 8, 'The Unofficial Amrita Amaravati Handbook', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.set_font('helvetica', 'B', 14)
        self.set_text_color(185, 28, 28) # Amrita Red
        self.cell(0, 10, 'Freshers Survival Sheet', align='C', new_x='LMARGIN', new_y='NEXT')
        
        self.set_text_color(0, 0, 0)
        self.ln(5)
        self.set_draw_color(229, 231, 235)
        self.line(10, 105, 200, 105)
        self.set_y(110)

    def section_title(self, title):
        self.ln(6)
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 8, title.upper(), align='L', new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)
        self.set_font('helvetica', '', 10)

    def add_bullet(self, text):
        self.set_font('helvetica', '', 10)
        self.cell(0, 6, f"- {text}", new_x='LMARGIN', new_y='NEXT')
        
    def add_check(self, text):
        self.set_font('helvetica', '', 10)
        self.cell(0, 6, f"[ x ] {text}", new_x='LMARGIN', new_y='NEXT')

    def add_text(self, text):
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, 6, text, new_x='LMARGIN', new_y='NEXT')
        
    def add_quote(self, text):
        self.ln(10)
        self.set_font('helvetica', 'I', 11)
        self.set_text_color(90, 100, 116)
        self.multi_cell(0, 6, f'"{text}"', align='C', new_x='LMARGIN', new_y='NEXT')

pdf = PDF()
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
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(185, 28, 28)
pdf.cell(0, 6, 'Attendance below 75% = FA', new_x='LMARGIN', new_y='NEXT')
pdf.set_text_color(0, 0, 0)
pdf.add_text('Do not gamble with attendance.')

# SECTION 3
pdf.section_title('Digital Lifelines')
pdf.set_font('helvetica', 'B', 10)
pdf.cell(20, 6, 'AUMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 10)
pdf.cell(0, 6, 'Academics, Attendance, Grades.', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('helvetica', 'B', 10)
pdf.cell(20, 6, 'GPMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 10)
pdf.cell(0, 6, 'Hostel and Campus Services.', new_x='LMARGIN', new_y='NEXT')

# SECTION 4
pdf.section_title('First Month Checklist')
pdf.add_check('Join one club.')
pdf.add_check('Attend induction events.')
pdf.add_check('Learn AUMS.')
pdf.add_check('Locate classrooms.')
pdf.add_check('Make friends outside your branch.')

# Force new page to avoid awkward breaking
pdf.add_page()

# SECTION 5
pdf.section_title('Clubs Worth Exploring')
pdf.add_bullet('Chakravyuha')
pdf.add_bullet('ACM')
pdf.add_bullet('IEEE')
pdf.add_bullet('Team bi0s')
pdf.add_bullet('AYUDH')
pdf.add_bullet('E-Cell')

# SECTION 6
pdf.section_title('Five Things To Remember')
pdf.add_text('1. Attendance below 75% is dangerous.')
pdf.add_text('2. Join clubs early.')
pdf.add_text('3. Build projects from Semester 1.')
pdf.add_text('4. Protect CGPA early.')
pdf.add_text('5. Make friends outside your branch.')

# SECTION 7
pdf.section_title('Senior Advice')
pdf.add_text('Do not wait until second year to start building.')
pdf.add_text('The students who start in Semester 1 gain an enormous advantage.')

# SECTION 8
pdf.section_title('Emergency Reminder')
pdf.set_font('helvetica', 'B', 10)
pdf.add_text('Screenshot this sheet. Keep a copy on your phone.')

# BOTTOM QUOTE
pdf.add_quote("One day you'll know every shortcut on campus. Until then, keep this sheet.")

pdf.output('survival-sheet.pdf')
