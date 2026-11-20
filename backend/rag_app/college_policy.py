"""
Halcyon Institute of Applied Sciences - Student Policy Manual
Version 1.0 | Effective 1 January 2027

Contains the complete text and page definitions from the SRS specification,
plus a generator to build a pristine 10-page PDF document.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

COLLEGE_POLICY_PAGES = [
    {
        "page_number": 1,
        "title": "Cover & Introduction",
        "sections": ["Title", "Introduction"],
        "text": """Halcyon Institute of Applied Sciences
Student Policy Manual
Version 1.0 | Effective 1 January 2027

This manual sets out the official policies that govern academic life, student conduct, and campus services at the Institute. It applies to all enrolled students and must be read together with the programme handbook of each school."""
    },
    {
        "page_number": 2,
        "title": "Preface and Authority & Table of Contents",
        "sections": ["Preface and Authority", "Contents"],
        "text": """Preface and Authority
This manual is issued under the authority of the Board of Governors and administered by the Office of the Registrar. Where a policy conflicts with applicable national or state law, the law prevails. The Institute may amend these policies from time to time; the current version is always the one published on the student portal.

Students are responsible for knowing the contents of this manual. Ignorance of a policy is not a defence to an alleged breach.

Contents
Policy 1 Academic Integrity Policy
Policy 2 Grading and Academic Standing Policy
Policy 3 Attendance Policy
Policy 4 Admissions Policy
Policy 5 Tuition, Fees and Refund Policy
Policy 6 Student Code of Conduct
Policy 7 Anti-Harassment and Non-Discrimination Policy
Policy 8 Housing and Residence Life Policy
Policy 9 Information Technology and Acceptable Use Policy
Policy 10 Library and Learning Resources Policy
Policy 11 Health, Safety and Emergency Response Policy
Policy 12 Research Ethics Policy
Policy 13 Student Appeals Policy"""
    },
    {
        "page_number": 3,
        "title": "Policy 1: Academic Integrity & Policy 2: Grading (Part 1)",
        "sections": ["Policy 1: Academic Integrity Policy", "Policy 2: Grading and Academic Standing Policy"],
        "text": """Policy 1: Academic Integrity Policy
Purpose: To protect the value of every credential awarded by the Institute by requiring honest, original work from all students.
Scope: Applies to all students in every program, course, examination, laboratory, thesis, and research activity, on campus and online.

Policy Statements
1.1 Academic dishonesty includes plagiarism, unauthorized collaboration, cheating on examinations, falsification or fabrication of data, submission of work previously graded in another course without approval, and contract cheating of any kind.
1.2 Students must cite all sources, including AI-generated text, code, and images, in the manner specified by the course instructor.
1.3 Instructors must state their collaboration and tool-use rules in the course syllabus at the start of each term.
1.4 Examinations are conducted under the supervision of invigilators. Devices not permitted by the examination instructions must be switched off and placed out of reach.
1.5 Students who witness suspected misconduct are encouraged to report it to the Office of Academic Standards.

Procedures
1. An instructor who suspects a violation must inform the student in writing within ten working days and provide the evidence.
2. The student may respond within five working days. If the matter is not resolved between the instructor and the student, it is referred to the Academic Integrity Panel.
3. Sanctions range from a reduced grade on the assignment to failure of the course, suspension, or expulsion, depending on severity and repeat offences.
4. Every finding is recorded in the student's confidential conduct file. Students may appeal under Policy 13.

Policy 2: Grading and Academic Standing Policy
Purpose: To define how academic performance is measured, recorded, and used to determine progression, probation, and graduation.
Scope: Applies to all undergraduate and postgraduate students enrolled in credit-bearing programs.

Policy Statements
2.1 Letter grades run from A (excellent) to F (fail) on a 4.0 grade-point scale. Grades of I (incomplete), W (withdrawn), and P (pass, for designated courses) are recorded without affecting the grade-point average.
2.2 The Cumulative Grade Point Average (CGPA) is calculated over all graded credits and is recalculated at the end of each term."""
    },
    {
        "page_number": 4,
        "title": "Policy 2: Grading (Part 2), Policy 3: Attendance, Policy 4: Admissions (Part 1)",
        "sections": ["Policy 2: Procedures", "Policy 3: Attendance Policy", "Policy 4: Admissions Policy"],
        "text": """2.3 A student whose CGPA falls below 2.0 at the end of any term is placed on Academic Probation. Two consecutive terms on probation may result in Academic Dismissal.
2.4 A minimum of 75 percent of attempted credits must be successfully completed each academic year to remain in good standing.
2.5 Grade changes after official publication require approval of the Dean of the relevant school and must be justified in writing.

Procedures
1. Students may request a review of a final grade within 14 days of publication by submitting the Grade Review Form to the Registrar.
2. An incomplete grade must be resolved within 30 days of the end of term, otherwise it converts automatically to an F.
3. Students on probation must meet with a faculty advisor and agree a written academic recovery plan.

Policy 3: Attendance Policy
Purpose: To ensure students receive the instruction and practical experience that each course requires.
Scope: Applies to all scheduled lectures, tutorials, laboratories, studios, clinical placements, and field work.

Policy Statements
3.1 Attendance is compulsory in laboratories, studios, clinical placements, and any session designated as mandatory in the course outline.
3.2 For other sessions, a student who misses more than 20 percent of scheduled contact hours in a course may be barred from the final examination in that course.
3.3 Absences due to illness, bereavement, official Institute representation, or religious observance are excused when supported by documentation submitted within five working days.
3.4 Attendance is recorded electronically. Students are responsible for verifying their own records each fortnight through the student portal.

Procedures
1. A student who expects a prolonged absence (more than five consecutive days) must notify the Dean of Students at the earliest opportunity.
2. Where an absence is excused, the instructor will provide reasonable opportunity to make up missed work or practicals.
3. Students who are barred from an examination due to attendance may appeal under Policy 13 within seven days of notification.

Policy 4: Admissions Policy
Purpose: To select applicants who are academically prepared and likely to succeed, using fair and transparent criteria."""
    },
    {
        "page_number": 5,
        "title": "Policy 4: Admissions (Part 2) & Policy 5: Tuition, Fees and Refund (Part 1)",
        "sections": ["Policy 4: Admissions Policy", "Policy 5: Tuition, Fees and Refund Policy"],
        "text": """Scope: Applies to all applications for undergraduate, postgraduate, and diploma programs, including transfer and mature-age applications.

Policy Statements
4.1 Admission decisions are based on prior academic achievement, standardized assessment results where required, a personal statement, and, for selected programs, an interview or portfolio review.
4.2 Applicants must hold a recognized secondary qualification or equivalent. Foreign qualifications are assessed by the Credentials Evaluation Office.
4.3 Admission is offered without regard to race, colour, caste, religion, sex, gender identity, sexual orientation, disability, nationality, or socio-economic background, except where a lawful affirmative-action or reserved-seat scheme applies.
4.4 The Institute reserves a fixed proportion of seats for students from economically disadvantaged backgrounds, as set by the Board of Governors each admissions cycle.
4.5 An offer is conditional until all final transcripts and identity documents are verified. Offers obtained through falsified documents are withdrawn.

Procedures
1. Applications close on the published deadline for each intake. Late applications are considered only if places remain.
2. Applicants are notified of decisions within 30 days of a complete application being received.
3. An offer must be accepted, and the enrolment deposit paid, within 21 days. Otherwise the place is released.

Policy 5: Tuition, Fees and Refund Policy
Purpose: To set out how fees are charged, when they are due, and under what circumstances they may be refunded.
Scope: Applies to all tuition, examination, laboratory, library, hostel, and administrative fees charged by the Institute.

Policy Statements
5.1 Tuition and fees are published annually in the Fee Schedule. The Institute may revise fees with at least 90 days' written notice to enrolled students.
5.2 Fees are payable in two instalments per academic year, due on the first day of each semester. Late payment attracts a surcharge of 2 percent per month.
5.3 Students with outstanding dues may not register for examinations, receive transcripts, or obtain degree certificates.
5.4 Scholarships and bursaries are credited against tuition and do not reduce the amount due for non-tuition fees.

Procedures
1. Withdrawal before the first day of teaching entitles the student to a refund of 90 percent of tuition, less the non-refundable registration fee."""
    },
    {
        "page_number": 6,
        "title": "Policy 5: Tuition (Part 2), Policy 6: Code of Conduct, Policy 7: Anti-Harassment (Part 1)",
        "sections": ["Policy 5: Procedures", "Policy 6: Student Code of Conduct", "Policy 7: Anti-Harassment and Non-Discrimination Policy"],
        "text": """2. Withdrawal within the first two weeks of teaching entitles the student to a 50 percent refund of tuition.
3. No tuition refund is available after the second week of teaching, except on documented medical or compassionate grounds approved by the Bursar.
4. Refunds are processed within 30 working days to the original payment method.

Policy 6: Student Code of Conduct
Purpose: To maintain a safe, respectful, and lawful environment in which every member of the community can learn and work.
Scope: Applies to all students on campus, in Institute housing, at Institute-sponsored events, during off-campus placements, and in online spaces associated with the Institute.

Policy Statements
6.1 Students are expected to treat fellow students, staff, visitors, and neighbours with courtesy and respect.
6.2 The following are prohibited: violence or threats of violence, bullying, stalking, property damage, theft, possession of weapons, and unlawful possession or distribution of controlled substances.
6.3 The consumption of alcohol is permitted only in designated areas and at events licensed by the Institute. Smoking and vaping are prohibited on all campus premises.
6.4 Students must carry their Institute identity card and produce it on request to authorized staff.
6.5 Students are responsible for the conduct of their guests.

Procedures
1. Alleged violations may be reported to the Dean of Students in person, by email, or through the anonymous reporting line.
2. Minor breaches may be resolved by a written warning or a restorative conversation. Serious breaches are referred to the Student Conduct Committee.
3. Possible sanctions include a formal warning, restitution, loss of privileges, suspension, or expulsion. Interim measures may be imposed while an investigation is under way.

Policy 7: Anti-Harassment and Non-Discrimination Policy
Purpose: To prevent and respond promptly to harassment, discrimination, and sexual misconduct, and to support everyone who reports them.
Scope: Applies to all students, staff, faculty, contractors, and visitors, in all Institute activities and communications.

Policy Statements
7.1 Harassment, including sexual harassment, is unwelcome conduct based on a protected characteristic that interferes with a person's education, work, or participation in campus life."""
    },
    {
        "page_number": 7,
        "title": "Policy 7: Anti-Harassment (Part 2), Policy 8: Housing, Policy 9: IT (Part 1)",
        "sections": ["Policy 7: Anti-Harassment Policy", "Policy 8: Housing and Residence Life Policy", "Policy 9: IT Policy"],
        "text": """7.2 Retaliation against anyone who makes a good-faith report or participates in an investigation is itself a serious violation.
7.3 The Institute will provide reasonable accommodation for students with disabilities, pregnancy, or religious needs, subject to the Accessibility Office's assessment.
7.4 All reports are handled confidentially, shared only on a need-to-know basis, and reviewed by trained investigators who are independent of the respondent's school or department.

Procedures
1. Complainants may report to the Equal Opportunity Office, the Counselling Centre, any faculty member, or the Dean of Students. Reports may be made at any time, though prompt reporting assists the investigation.
2. Investigations are normally completed within 60 days. Both parties receive written notice of the outcome and a right of appeal to the Vice-Chancellor.
3. Supportive measures, such as changes in class schedule, housing, or reporting lines, may be provided at any stage regardless of the outcome.

Policy 8: Housing and Residence Life Policy
Purpose: To provide safe, well-maintained residential accommodation that supports student wellbeing and community living.
Scope: Applies to all students living in Institute halls of residence and any Institute-leased accommodation.

Policy Statements
8.1 Residence is allocated by the Housing Office on the basis of application date, programme, and any accessibility needs. Priority is given to first-year and international students.
8.2 Residents must sign a residence agreement covering a full academic year. Early termination requires one term's written notice and may incur a charge.
8.3 Quiet hours apply from 22:00 to 07:00 on all nights, and extended during examination periods.
8.4 Visitors are permitted in common areas during published visiting hours. Overnight guests require the resident's roommate's consent and prior registration at the front desk.
8.5 Residents are responsible for damage to their rooms beyond normal wear and tear.

Procedures
1. Maintenance requests must be logged through the residence portal. Emergencies must be reported to the duty warden immediately.
2. Room inspections are carried out twice per term with 48 hours' notice, except where there is a documented safety concern.
3. Breaches of the residence agreement are handled under the Student Code of Conduct.

Policy 9: Information Technology and Acceptable Use Policy"""
    },
    {
        "page_number": 8,
        "title": "Policy 9: IT Policy (Part 2) & Policy 10: Library and Learning Resources",
        "sections": ["Policy 9: IT Policy", "Policy 10: Library and Learning Resources Policy"],
        "text": """Purpose: To protect the confidentiality, integrity, and availability of the Institute's information systems and the data held within them.
Scope: Applies to all users of Institute networks, devices, email accounts, learning platforms, and cloud services, whether on campus or remotely.

Policy Statements
9.1 Login credentials are personal and must not be shared. Multi-factor authentication is required for all student accounts.
9.2 Institute systems may be used for academic, research, and administrative purposes. Limited personal use is permitted provided it does not disrupt operations or breach this policy.
9.3 The following are prohibited: attempting to access systems or data without authorization, installing malicious software, using the network for commercial activity unrelated to the Institute, and sending unsolicited bulk messages.
9.4 Personal data of students and staff must be handled in accordance with the Institute's Data Protection Standard and applicable privacy law.
9.5 Users must report suspected security incidents to the IT Service Desk within 24 hours of discovery.

Procedures
1. The Institute may monitor systems for security and maintenance purposes. Monitoring of individual communications requires written approval from the Chief Information Officer.
2. Access to a student's account after departure is revoked 30 days after the last day of enrolment, unless an extension is approved.
3. Breaches may result in suspension of access and referral under the Student Code of Conduct.

Policy 10: Library and Learning Resources Policy
Purpose: To give all students fair and reliable access to library materials, study spaces, and digital learning resources.
Scope: Applies to all students, and to alumni and visiting researchers where specifically authorized.

Policy Statements
10.1 Undergraduate students may borrow up to 10 items for 28 days. Postgraduate students may borrow up to 20 items for 56 days.
10.2 Items may be renewed once, unless they have been reserved by another user.
10.3 Overdue items attract a fine of 10 INR per item per day. Fines exceeding 500 INR block further borrowing until settled.
10.4 Digital resources are licensed for educational use only. Systematic downloading or sharing of licensed content outside the Institute is prohibited.

Procedures
1. Lost or damaged items must be reported immediately. The replacement cost plus a processing fee is charged to the borrower."""
    },
    {
        "page_number": 9,
        "title": "Policy 10: Library (Part 2), Policy 11: Health & Safety, Policy 12: Research Ethics (Part 1)",
        "sections": ["Policy 10: Procedures", "Policy 11: Health, Safety and Emergency Response Policy", "Policy 12: Research Ethics Policy"],
        "text": """2. Quiet study areas must be kept silent. Food and drink are permitted only in designated zones.

Policy 11: Health, Safety and Emergency Response Policy
Purpose: To protect the physical and mental health of students and to ensure a prepared response to emergencies on campus.
Scope: Applies to all campus premises, laboratories, workshops, field placements, and Institute-sponsored travel.

Policy Statements
11.1 All laboratory and workshop users must complete safety induction and wear prescribed protective equipment before commencing work.
11.2 Students with a known medical condition are encouraged to register with the Health Centre so that appropriate support can be arranged in an emergency.
11.3 Every incident, near-miss, or injury must be reported through the incident system within 24 hours.
11.4 The Institute operates a counselling service offering confidential support on academic, personal, and mental health concerns, available free of charge to all enrolled students.

Procedures
1. In a medical emergency, call the campus emergency number first, then notify the Health Centre and the Dean of Students.
2. Evacuation drills are held at least twice per academic year in all residential and teaching buildings.
3. Students on placements must follow the host organization's safety rules and report any concern to their supervising faculty member.

Policy 12: Research Ethics Policy
Purpose: To ensure that all research conducted under the Institute's name meets the highest standards of integrity, safety, and respect for participants.
Scope: Applies to all research by students, faculty, and staff, including thesis work, funded projects, and collaborations.

Policy Statements
12.1 Research involving human participants, animals, or sensitive personal data must receive approval from the Research Ethics Committee before data collection begins.
12.2 Participation must be voluntary and based on informed consent. Participants may withdraw at any time without penalty.
12.3 Research findings must be reported accurately. Selective reporting, manipulation of results, and undisclosed conflicts of interest are research misconduct.
12.4 Research data must be retained for at least five years after publication, in secure storage consistent with the data protection standard."""
    },
    {
        "page_number": 10,
        "title": "Policy 12: Research (Part 2), Policy 13: Student Appeals & Review",
        "sections": ["Policy 12: Procedures", "Policy 13: Student Appeals Policy", "Review and Revision"],
        "text": """Procedures
1. Allegations of research misconduct are referred to the Research Integrity Officer, who determines whether a formal inquiry is required.
2. Students may appeal a decision of the Research Ethics Committee to the Academic Board within 21 days.

Policy 13: Student Appeals Policy
Purpose: To provide a fair, timely, and independent route for students who believe a decision affecting them was wrong or unfair.
Scope: Applies to decisions on grades, academic integrity, attendance, conduct, fees, and housing, unless another policy sets out a specific appeal route.

Policy Statements
13.1 A student may appeal a decision on the grounds of procedural error, new evidence not reasonably available earlier, or a decision that was unreasonable in light of the evidence.
13.2 Dissatisfaction with the outcome alone is not a ground of appeal.
13.3 Appeals must be submitted in writing to the Office of the Registrar within the deadline stated in the relevant policy, or within 14 days of the decision where none is stated.
13.4 An appeal is heard by a panel that did not take part in the original decision. Students may be accompanied by a companion or adviser at any hearing.

Procedures
1. The Registrar acknowledges receipt within five working days and confirms whether the appeal is admissible.
2. The appeal panel issues a written decision within 30 working days, giving reasons. This decision is final within the Institute, save for any statutory right of external review.

Review and Revision
Each policy in this manual is reviewed by its owning office at least once every three years, or sooner where legislation or institutional priorities change. Proposed revisions are submitted to the Academic Board for approval. Students may submit feedback through the Registrar's office at any time.

Approved by the Board of Governors. Version 1.0, effective 1 January 2027."""
    }
]

class NumberedCanvas(canvas.Canvas):
    """Adds running headers and footers with page numbers matching the SRS format."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        if page_num > 1:
            # Header
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#4b5563"))
            self.drawString(54, 750, "Halcyon Institute of Applied Sciences | Student Policy Manual | Effective 1 January 2027")
            self.drawRightString(558, 750, f"Page {page_num}")
            self.setStrokeColor(colors.HexColor("#e5e7eb"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)

            # Footer
            self.setStrokeColor(colors.HexColor("#e5e7eb"))
            self.setLineWidth(0.5)
            self.line(54, 45, 558, 45)
            self.setFont("Helvetica", 8)
            self.drawString(54, 32, "Halcyon Institute of Applied Sciences | Student Policy Manual | Effective 1 January 2027")
            self.drawRightString(558, 32, f"Page {page_num}")
        self.restoreState()


def generate_halcyon_pdf(output_path: str):
    """Generates an authentic 10-page PDF matching the OCR text and layout."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=64,
        bottomMargin=54
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor('#1e3a8a'),
        alignment=1, # Center
        spaceAfter=15
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1f2937'),
        alignment=1,
        spaceAfter=10
    )
    version_style = ParagraphStyle(
        'CoverVersion',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#4b5563'),
        alignment=1,
        spaceAfter=80
    )
    cover_desc = ParagraphStyle(
        'CoverDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#374151'),
        alignment=1,
        spaceAfter=20
    )
    h1_style = ParagraphStyle(
        'PolicyH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=10,
        spaceAfter=8
    )
    h2_style = ParagraphStyle(
        'PolicyH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#111827'),
        spaceBefore=8,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'PolicyBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=6
    )

    story = []

    for page_data in COLLEGE_POLICY_PAGES:
        p_num = page_data["page_number"]
        if p_num == 1:
            story.append(Spacer(1, 140))
            story.append(Paragraph("Halcyon Institute of Applied Sciences", title_style))
            story.append(Paragraph("Student Policy Manual", subtitle_style))
            story.append(Paragraph("Version 1.0 | Effective 1 January 2027", version_style))
            story.append(Spacer(1, 60))
            desc_text = ("This manual sets out the official policies that govern academic life, student "
                         "conduct, and campus services at the Institute. It applies to all enrolled students "
                         "and must be read together with the programme handbook of each school.")
            story.append(Paragraph(desc_text, cover_desc))
            story.append(PageBreak())
            continue

        lines = [line.strip() for line in page_data["text"].split('\n') if line.strip()]
        for line in lines:
            if line.startswith("Policy ") and ":" in line:
                story.append(Paragraph(line, h1_style))
            elif line in ["Preface and Authority", "Contents", "Review and Revision"]:
                story.append(Paragraph(line, h1_style))
            elif line in ["Policy Statements", "Procedures"]:
                story.append(Paragraph(line, h2_style))
            elif line.startswith("Purpose:") or line.startswith("Scope:"):
                key, val = line.split(":", 1)
                t = Table([[Paragraph(f"<b>{key}</b>", body_style), Paragraph(val.strip(), body_style)]], colWidths=[65, 435])
                t.setStyle(TableStyle([
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('TOPPADDING', (0,0), (-1,-1), 2),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
                ]))
                story.append(t)
            else:
                story.append(Paragraph(line, body_style))

        if p_num < len(COLLEGE_POLICY_PAGES):
            story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)
    return output_path


def get_college_policy_full_text():
    """Returns the concatenated text of the policy manual."""
    return "\n\n".join([f"--- Page {p['page_number']}: {p['title']} ---\n{p['text']}" for p in COLLEGE_POLICY_PAGES])
