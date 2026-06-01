import os

# Try to install fpdf2 silently
os.system('pip install fpdf2 > /dev/null 2>&1')

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 18)
        self.cell(0, 10, 'CAMPUS COMPASS', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('helvetica', 'I', 12)
        self.set_text_color(185, 28, 28) # Amrita Red
        self.cell(0, 10, 'Freshers Survival Sheet', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)
        self.ln(5)
        self.set_draw_color(229, 231, 235)
        self.line(10, 30, 200, 30)

    def section_title(self, title):
        self.ln(8)
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(15, 27, 45) # Navy
        self.cell(0, 8, title.upper(), align='L', new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)
        self.set_font('helvetica', '', 10)

    def add_bullet(self, text):
        self.set_font('helvetica', '', 10)
        self.cell(0, 6, f"- {text}", new_x='LMARGIN', new_y='NEXT')

    def add_text(self, text):
        self.set_font('helvetica', '', 10)
        self.cell(0, 6, text, new_x='LMARGIN', new_y='NEXT')

pdf = PDF()
pdf.add_page()

pdf.section_title('SECTION 1 - BEFORE YOU ARRIVE')
pdf.add_bullet('Admission Letter')
pdf.add_bullet('Aadhaar Copies')
pdf.add_bullet('Passport Photos')
pdf.add_bullet('Laptop + Charger')
pdf.add_bullet('Medical Documents')

pdf.section_title('SECTION 2 - RULES NOBODY EXPLAINS')
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(185, 28, 28)
pdf.cell(0, 6, 'Attendance below 75% = FA', new_x='LMARGIN', new_y='NEXT')
pdf.set_text_color(0, 0, 0)
pdf.add_text('Do not gamble with attendance.')

pdf.section_title('SECTION 3 - DIGITAL LIFELINES')
pdf.set_font('helvetica', 'B', 10)
pdf.cell(20, 6, 'AUMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 10)
pdf.cell(0, 6, 'Academics, grades, attendance.', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('helvetica', 'B', 10)
pdf.cell(20, 6, 'GPMS:', new_x='RIGHT')
pdf.set_font('helvetica', '', 10)
pdf.cell(0, 6, 'Hostel and campus services.', new_x='LMARGIN', new_y='NEXT')

pdf.section_title('SECTION 4 - FIRST MONTH CHECKLIST')
pdf.add_bullet('Join at least one club.')
pdf.add_bullet('Attend induction events.')
pdf.add_bullet('Learn AUMS.')
pdf.add_bullet('Locate classrooms.')
pdf.add_bullet('Build friendships outside your branch.')

pdf.section_title('SECTION 5 - CLUBS TO EXPLORE')
pdf.add_bullet('Chakravyuha')
pdf.add_bullet('ACM')
pdf.add_bullet('IEEE')
pdf.add_bullet('Team bi0s')
pdf.add_bullet('AYUDH')
pdf.add_bullet('E-Cell')

pdf.section_title('SECTION 6 - SENIOR ADVICE')
pdf.add_text('Do not wait until second year to start building.')
pdf.add_text('The students who begin projects in Semester 1 gain an enormous advantage.')

pdf.section_title('SECTION 7 - EMERGENCY REMINDER')
pdf.add_text('Screenshot this sheet. Keep a copy on your phone.')

pdf.output('survival-sheet.pdf')
