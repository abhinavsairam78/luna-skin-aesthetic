import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.units import inch

def create_manual_pdf(filename="USER_MANUAL.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    styles = getSampleStyleSheet()
    
    # Color Palette
    PRIMARY = colors.HexColor("#5F7D6E")
    SECONDARY = colors.HexColor("#5C4E48")
    ACCENT = colors.HexColor("#C29957")
    BG_LIGHT = colors.HexColor("#FAF9F6")
    TEXT_DARK = colors.HexColor("#2A2624")
    LINE_COLOR = colors.HexColor("#EBE4DC")
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'Heading1Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=SECONDARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_DARK,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        leftIndent=12,
        spaceAfter=4
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=TEXT_DARK
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13.5,
        textColor=PRIMARY
    )

    story = []
    
    # Header Banner
    story.append(Paragraph("📖 Luna Skin Aesthetics", title_style))
    story.append(Paragraph("Complete Operating Manual — A to Z Guide for Specialist & Staff Operations", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=PRIMARY, spaceBefore=0, spaceAfter=12))
    
    # Quick Reference Table
    quick_ref_data = [
        [Paragraph("Resource", table_header), Paragraph("Information & Credentials", table_header)],
        [Paragraph("Website URL", table_cell), Paragraph("<b>https://lunaskinaesthetics.com</b>", table_cell)],
        [Paragraph("Clinic Address", table_cell), Paragraph("200K/5, Seyad plaza, Tiruchendur main road, palayamkottai, Tirunelveli, Tamil Nadu 627002", table_cell)],
        [Paragraph("Contact Phone (SMS Alerts)", table_cell), Paragraph("<b>9025676090</b> (+91 90256 76090)", table_cell)],
        [Paragraph("Clinic Email", table_cell), Paragraph("<b>lunaskinaesthetics24@gmail.com</b>", table_cell)],
        [Paragraph("Lead Specialist", table_cell), Paragraph("<b>Dr. Krithika SK</b> (Lead Clinical Cosmetologist & Dermatologist)", table_cell)],
        [Paragraph("Specialist Portal Login", table_cell), Paragraph("Email: <b>lunaskinaesthetics24@gmail.com</b> | Password: <b>krithika2026</b>", table_cell)],
    ]
    
    t_quick = Table(quick_ref_data, colWidths=[2.2*inch, 5.3*inch])
    t_quick.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, LINE_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [BG_LIGHT, colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_quick)
    story.append(Spacer(1, 10))
    
    # Section 1: Specialist Portal
    story.append(Paragraph("1. Specialist Portal Operations (Dr. Krithika SK)", h1_style))
    story.append(Paragraph("<b>1.1 Logging In & iPad Setup</b>", h2_style))
    story.append(Paragraph("• Visit <b>https://lunaskinaesthetics.com</b> on any browser or iPad Safari.", bullet_style))
    story.append(Paragraph("• Click <b>Specialist Portal</b> in top navigation → Select <b>Specialist</b> tab.", bullet_style))
    story.append(Paragraph("• Enter Email: <b>lunaskinaesthetics24@gmail.com</b> and Password: <b>krithika2026</b>.", bullet_style))
    story.append(Paragraph("• <i>iPad Safari Tip</i>: Tap <b>Share → Add to Home Screen</b> to install as a full-screen native iPad application.", bullet_style))
    
    story.append(Paragraph("<b>1.2 Patient Directory Roster</b>", h2_style))
    story.append(Paragraph("• Click <b>Patient List</b> on top navigation header.", bullet_style))
    story.append(Paragraph("• Search patient by Name, Ref ID (e.g., <i>LSA-2026-61201</i>), or Primary Concern.", bullet_style))
    story.append(Paragraph("• Click <b>Open Case Sheet</b> to view/edit medical records, or <b>Delete</b> to remove.", bullet_style))

    story.append(Paragraph("<b>1.3 Creating New Patient Record</b>", h2_style))
    story.append(Paragraph("• Click <b>+ CREATE PATIENT RECORD</b> button.", bullet_style))
    story.append(Paragraph("• Enter Name, Age, Gender, Contact, Skin Type, Primary Concern, and Allergies.", bullet_style))
    story.append(Paragraph("• Click <b>Save Record</b>. The system assigns a unique Ref ID (<i>LSA-YYYY-XXXXX</i>) and auto-assigns the record under Dr. Krithika SK.", bullet_style))

    story.append(Paragraph("<b>1.4 Managing Patient Case Sheets</b>", h2_style))
    story.append(Paragraph("• <b>Section I (Personal Details)</b>: Edit contact info, allergies, medications, daily skincare routine. Edits auto-save with real-time <i>Draft Saved</i> indicator.", bullet_style))
    story.append(Paragraph("• <b>Section II (Diagnostic Analysis)</b>: Select Skin Type, check clinical concerns (Hyperpigmentation, Acne Grade 1-4, Elasticity, Dehydration), and input Practitioner Observations.", bullet_style))
    story.append(Paragraph("• <b>Section III (Protocol & Prescriptions)</b>: Edit 3-Phase Corrective Plans. Click <i>+ Add Procedure</i> for history or <i>+ Prescribe Product</i> to prescribe skincare units.", bullet_style))
    story.append(Paragraph("• <b>Section IV (Therapy Timeline Logs)</b>: Click <i>+ Add Log Entry</i> after each session to record Date, Therapy, Client Reaction, and Notes.", bullet_style))
    story.append(Paragraph("• <b>Section V (Appointment Scheduler)</b>: View appointments or click <i>Schedule Follow-up</i> to pick date, time slot, and purpose.", bullet_style))
    story.append(Paragraph("• <b>Section VI (Clinical Photography)</b>: Upload high-resolution <i>Before</i> and <i>After</i> photos. Drag the <i>Split Drag Slider</i> to compare progress side-by-side.", bullet_style))

    story.append(Paragraph("<b>1.5 Protocol Verification & PDF Export</b>", h2_style))
    story.append(Paragraph("• Scroll to <b>Protocol Verification & Sign-off</b> → Click <b>Verify & Sign Protocol</b> to lock file with digital hash <i>#882-LUNA-SAFE-921</i>.", bullet_style))
    story.append(Paragraph("• Click <b>Export PDF</b> on top action bar to print or save a PDF copy for medical records.", bullet_style))

    story.append(Spacer(1, 8))

    # Section 2: Appointments & Google Calendar
    story.append(Paragraph("2. Appointment System & Google Calendar Sync", h1_style))
    story.append(Paragraph("• <b>Purple Appointment Dots</b>: Calendar days render dots on days with client visits. Click any date to open the Day Schedule panel.", bullet_style))
    story.append(Paragraph("• <b>Automated Email Alerts</b>: Every appointment request dispatches email notifications to <b>lunaskinaesthetics24@gmail.com</b>.", bullet_style))
    story.append(Paragraph("• <b>SMS Notifications</b>: Instant SMS alerts logged to Clinic phone <b>9025676090</b>.", bullet_style))
    story.append(Paragraph("• <b>Google Calendar Sync</b>: Booking confirmations render a direct <b>Add to Google Calendar</b> link and a downloadable <b>.ics Calendar File</b>.", bullet_style))

    story.append(Spacer(1, 8))

    # Section 3: Patient Portal & Landing Page
    story.append(Paragraph("3. Patient Portal & Landing Page Experience", h1_style))
    story.append(Paragraph("• <b>Patient Self-Registration</b>: Clients register via <i>New Client Registration</i> button and log in to view personal skincare routines and appointment status.", bullet_style))
    story.append(Paragraph("• <b>Interactive Skincare Assessor</b>: Homepage visitors select Skin Type and Main Concern for instant clinical regimen recommendations.", bullet_style))
    story.append(Paragraph("• <b>Before/After Photo Comparison Slider</b>: Visual demonstration of non-invasive clinical results.", bullet_style))

    story.append(Spacer(1, 8))

    # Section 4: Clinic Settings & Theme Customization
    story.append(Paragraph("4. Clinic Settings & Theme Customization", h1_style))
    story.append(Paragraph("• <b>Clinic Settings (⚙️)</b>: Edit Clinic Name, Lead Dermatologist, License ID, Address, Phone, or Email.", bullet_style))
    story.append(Paragraph("• <b>Theme Switcher (🌙/☀️)</b>: Toggle between Luminous Light Mode and Sleek Dark Mode.", bullet_style))
    story.append(Paragraph("• <b>Data Persistence</b>: All edits auto-save to <i>data/patients.json</i> and browser local storage for complete offline/serverless continuity.", bullet_style))

    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=4, spaceAfter=8))
    
    footer_text = ParagraphStyle(
        'FooterText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=SECONDARY,
        alignment=1
    )
    story.append(Paragraph("Luna Skin Aesthetics — Confidential Clinical Operating Manual — 200K/5, Seyad plaza, Tiruchendur main road, palayamkottai, Tirunelveli, Tamil Nadu 627002", footer_text))

    doc.build(story)
    print(f"Successfully generated {filename}")

if __name__ == '__main__':
    create_manual_pdf()
