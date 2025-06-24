from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, Image, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import random
import os
import string
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# --- Data Collection Functions (KEEP THESE AS THEY ARE) ---
def collect_personal_info():
    print("Enter Personal Information:")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")
    linkedin = input("LinkedIn: ") 
    github = input("Github: ") 
    portfolio = input("Portfolio: ")  
    return {"Name": name, "Email": email, "Phone": phone, "Address": address, "LinkedIn":linkedin, "Github":github,"Portfolio":portfolio}

def collect_education():
    education_list = []
    while True:
        print("\nEnter Education Details (leave degree blank to stop):")
        degree = input("Degree/Certificate: ")
        if not degree:
            break
        institution = input("Institution: ")
        cgpa=input("CGPA: ")
        year = input("Year of Completion (e.g., 2020 or Present): ")
        education_list.append({"Degree": degree, "Institution": institution, "Year": year,"CGPA":cgpa})
    return education_list

def collect_experience():
    experience_list = []
    while True:
        print("\nEnter Work Experience (leave job title blank to stop):")
        job_title = input("Job Title: ")
        if not job_title:
            break
        company = input("Company: ")
        duration = input("Duration (e.g., Jan 2023 - Present): ")
        print("Enter Job Description (type 'DONE' on a new line to finish):")
        description_lines = []
        while True:
            line = input(" - ") # Added a prompt for each line
            if line.upper() == 'DONE':
                break
            description_lines.append(line)
        experience_list.append({"Job Title": job_title, "Company": company, "Duration": duration, "Description": description_lines})
    return experience_list

def collect_skills():
    print("\nEnter Skills (comma-separated, e.g., Python, Java, SQL):")
    skills = input("Skills: ").split(", ")
    return [skill.strip() for skill in skills if skill.strip()]

def collect_projects():
    project_list = []
    while True:
        print("\nEnter Project Details (leave project name blank to stop):")
        project_name = input("Project Name: ")
        if not project_name:
            break
        description = input("Project Description: ")
        technologies = input("Technologies Used: ")
        project_list.append({"Project Name": project_name, "Description": description, "Technologies": technologies})
    return project_list

# --- NEW: Function to collect references (optional, as shown in image) ---
def collect_references():
    references_list = []
    while True:
        print("\nEnter Reference Details (leave name blank to stop):")
        name = input("Reference Name: ")
        if not name:
            break
        title = input("Reference Title/Company: ")
        contact = input("Reference Contact (Phone or Email): ")
        references_list.append({"Name": name, "Title": title, "Contact": contact})
    return references_list


def generate_pdf_resume1(personal_info, education, experience, skills, projects, references):
    
    filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + ".pdf"
    
    # Define page margins and dimensions
    left_margin = 0.75 * inch
    right_margin = 0.75 * inch
    top_margin = 0.75 * inch
    bottom_margin = 0.75 * inch
    

    # Calculate available content width and height
    page_width, page_height = letter
    available_width = page_width - left_margin - right_margin
    available_height = page_height - top_margin - bottom_margin

    # Define sidebar width
    sidebar_width = 2.2 * inch # Width of the purple sidebar
    

    # --- Create the SimpleDocTemplate instance FIRST ---
    # This must be done before defining content_offset_x if it depends on doc.leftMargin
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin
    )
    

    # Now define content_offset_x and content_width, as 'doc' is available
    content_offset_x = doc.leftMargin + sidebar_width + (0.2 * inch) # X-position for main content start
    content_width = available_width - sidebar_width - (0.2 * inch) # Width for the main content frame


    # Define styles
    styles = getSampleStyleSheet()

    # CUSTOMIZE/DEFINE STYLES (MATCHING THE IMAGE)
    # Section Heading for main content (Profile, Employment History, etc.)
    section_heading = ParagraphStyle(
        name='SectionHeading',
        parent=styles['h2'], # Use a standard heading as parent
        fontSize=12,
        textColor=colors.HexColor("#3d0c53"), # Dark purple from your image
        spaceBefore=12,
        spaceAfter=6,
        leading=14 # Line spacing
    )
    styles.add(section_heading)

    # Normal text style for main content
    normal_text_style = ParagraphStyle(
        name='NormalText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=4,
        leading=12 # Line spacing
    )
    styles.add(normal_text_style)


    # Bullet point style for job descriptions, project descriptions etc.
    bullet_text_style = ParagraphStyle(
        name='BulletText',
        parent=styles['Normal'], # Base it on Normal
        fontName='Helvetica',
        fontSize=10,
        leftIndent=15, # Indent for bullet
        firstLineIndent=-15, # To hang the bullet
        bulletIndent=5, # Space for the bullet itself
        spaceBefore=0,
        spaceAfter=2, # Tighter spacing for bullet points
        leading=12 # Line spacing
    )
    styles.add(bullet_text_style)

    # Style for employment history duration
    duration_style = ParagraphStyle(
        name='DurationStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique', # Italic
        fontSize=9,
        textColor=colors.grey, # Slightly lighter color
        spaceBefore=0,
        spaceAfter=2,
    )
    styles.add(duration_style)

    # Style for reference details
    reference_style = ParagraphStyle(
        name='ReferenceStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        spaceAfter=1
    )
    styles.add(reference_style)

    

    try: # The try block now only covers the 'build' and print statements.
         # The 'doc' instantiation and setup should be outside if needed by frames.

        # Define the frames that will hold the *flowable* content (main column)
        frames = [
            Frame(
                content_offset_x, # x1 (right of sidebar + gap)
                doc.bottomMargin, # y1 (bottom edge of frame)
                content_width,    # width
                available_height, # height (up to top margin)
                leftPadding=6,
                bottomPadding=6,
                rightPadding=6,
                topPadding=6,
                showBoundary=0 # Set to 1 for debugging frame boundaries
            )
        ]
        

        # Define the custom PageTemplate class - inherits directly from reportlab.platypus.PageTemplate
        class ResumePageTemplate(PageTemplate):
            def __init__(self, id, frames, sidebar_info, skill_list, onPage=None, onPageEnd=None):
                #PageTemplate.__init__(self, id, frames, onPage, onPageEnd)
                PageTemplate.__init__(self, id, frames, onPage=self.draw_sidebar, onPageEnd=self.beforeDrawPage)
                self.sidebar_info = sidebar_info
                self.skill_list = skill_list
                # Pre-calculate common y-positions if needed, or adjust dynamically

        # Renamed from beforeDrawPage to draw_sidebar for clarity and direct use as onPage
            def draw_sidebar(self, canvas_obj, doc_obj):
                canvas_obj.saveState()
                # Draw sidebar background (full height, extends to right edge of sidebar)
                canvas_obj.setFillColor(colors.HexColor("#3d0c53"))
                canvas_obj.rect(
                    0, 0,
                    left_margin + sidebar_width,
                    page_height,
                    fill=1, stroke=0
                )

                # Draw sidebar content directly onto the canvas (manual positioning)
                canvas_obj.setFillColor(colors.white)

            def beforeDrawPage(self, canvas_obj, doc_obj):
                canvas_obj.saveState()
                # Draw sidebar background (full height, extends to right edge of sidebar)
                canvas_obj.setFillColor(colors.HexColor("#3d0c53")) # Dark purple
                canvas_obj.rect(
                    0, 0, # Start from (0,0) of the page
                    left_margin + sidebar_width, # Width of the colored area
                    page_height, # Full page height
                    fill=1, stroke=0
                )

                # Draw sidebar content directly onto the canvas (manual positioning)
                canvas_obj.setFillColor(colors.white)


                # Profile Image
                image_path = r"swetha1.png" # Using relative path for better portability
                img_size = 1.0 * inch # Size from image
                if os.path.exists(image_path):
                    img_x = left_margin + sidebar_width/2 - img_size/2 # Center the image
                    img_y = page_height - top_margin - 30 - img_size # Position below top margin, adjusted
                    canvas_obj.drawImage(image_path, img_x, img_y, width=img_size, height=img_size, mask='auto')
                    current_y = img_y - 15 # Space after image
                else:
                    current_y = page_height - top_margin - 40 # If no image, start lower

                # Name (Sophie Walton style)
                canvas_obj.setFont('Helvetica-Bold', 16) # Adjust font size based on image
                canvas_obj.drawCentredString(left_margin + sidebar_width / 2, current_y, self.sidebar_info['Name'])
                current_y -= 20 # Space below name

                # Details Header
                canvas_obj.setFont('Helvetica-Bold', 10)
                canvas_obj.drawString(left_margin + 10, current_y, "DETAILS")
                current_y -= 15 # Space below header

                # Details Content
                canvas_obj.setFont('Helvetica', 9) # Smaller font for details
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['Address'])
                current_y -= 12
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['Phone'])
                current_y -= 12
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['Email'])
                current_y -= 20 # Space after details
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['LinkedIn'])
                current_y -= 20
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['Github'])
                current_y -= 20
                canvas_obj.drawString(left_margin + 10, current_y, self.sidebar_info['Portfolio'])
                current_y -= 20
                
                # Skills Header
                canvas_obj.setFont('Helvetica-Bold', 10)
                canvas_obj.drawString(left_margin + 10, current_y, "SKILLS")
                current_y -= 15 # Space below header

                # Skills List
                canvas_obj.setFont('Helvetica', 9) # Smaller font for skills
                for skill in self.skill_list:
                    canvas_obj.drawString(left_margin + 10, current_y, skill) # No bullet for skills in image
                    current_y -= 12
                current_y -= 20 # Space after skills section (you can add more sections here)
                
                # Create a canvas
                c = canvas.Canvas("language_bar_resume.pdf", pagesize=A4)
                width, height = A4

                # Colors
                purple = HexColor("#4B2059")
                light_gray = HexColor("#E0E0E0")

                # Draw left pane background
                left_pane_width = 2.5 * inch
                c.setFillColor(purple)
                c.rect(0, 0, left_pane_width, height, fill=True, stroke=False)

                # Set starting Y position
                start_y = height - inch

                # Add heading
                c.setFont("Helvetica-Bold", 12)
                c.setFillColor(white)
                c.drawString(0.4 * inch, start_y, "Languages")

                # Function to draw language proficiency bar
                def draw_language_bar(y, label, percent):
                    bar_x = 0.4 * inch
                    bar_y = y - 15
                    bar_width = left_pane_width - 0.8 * inch
                    bar_height = 8

                    # Draw label
                    c.setFont("Helvetica", 10)
                    c.drawString(bar_x, y, label)

                    # Background bar (gray)
                    c.setFillColor(light_gray)
                    c.rect(bar_x, bar_y, bar_width, bar_height, fill=True, stroke=False)

                    # Foreground bar (purple)
                    filled_width = bar_width * (percent / 100.0)
                    c.setFillColor(white)
                    c.rect(bar_x, bar_y, filled_width, bar_height, fill=True, stroke=False)

                # Example languages
                languages = [
                    ("English", 100),
                    ("Spanish", 75),
                    ("French", 50),
                ]

                # Draw each language
                y_pos = start_y - 30
                for lang, perc in languages:
                    draw_language_bar(y_pos, lang, perc)
                    y_pos -= 30


                canvas_obj.restoreState()


        # Add the custom page template to the document instance
        doc.addPageTemplates([
            ResumePageTemplate( # Renamed from SidebarPageTemplate for clarity
                id='ResumeTemplate',
                frames=frames, # Only the main content frame is passed here for flowables
                sidebar_info=personal_info,
                skill_list=skills
            )
        ])

        # --- Build Main Content (as a list of flowables) ---
        main_story = []

        # Profile Section
        main_story.append(Paragraph("Profile", section_heading))
        # TODO: Make this user input!
        main_story.append(Paragraph(
            "Dedicated Customer Service Representative dedicated to providing quality care to every customer interaction. Proven ability to resolve issues and maintain customer satisfaction. Exceptional communication skills combined with effective solutions to all problems. Excellent time management skills, committed to meeting goals and targets. Bilingual in English and Spanish. Willing to travel as needed.",
            normal_text_style)) # Use the new normal_text_style
        main_story.append(Spacer(1, 12))

        # Employment History Section
        main_story.append(Paragraph("Employment History", section_heading))
        for exp in experience:
            main_story.append(Paragraph(f"<b>{exp['Job Title']}</b>, {exp['Company']}", normal_text_style))
            main_story.append(Paragraph(exp['Duration'], duration_style)) # Use duration_style for dates
            for desc_line in exp['Description']:
                if desc_line.strip():
                    main_story.append(Paragraph(f"• {desc_line.strip()}", bullet_text_style))
            main_story.append(Spacer(1, 8)) # Space between job entries
        main_story.append(Spacer(1, 12))

        # Education Section
        main_story.append(Paragraph("Education", section_heading))
        for edu in education:
            main_story.append(Paragraph(f"<b>{edu['Degree']}</b>", normal_text_style))
            main_story.append(Paragraph(f"<b>{edu['Institution']}</b>", normal_text_style))
            main_story.append(Paragraph(f"<b>{edu['CGPA']}</b>", normal_text_style))
            if edu['Year']:
                main_story.append(Paragraph(edu['Year'], duration_style)) # Use duration style for year
            main_story.append(Spacer(1, 8))
        main_story.append(Spacer(1, 12))

        # Projects Section (if you want to keep this, it's not explicitly in the image)
        if projects:
            main_story.append(Paragraph("Projects", section_heading))
            for proj in projects:
                main_story.append(Paragraph(f"<b>{proj['Project Name']}</b>", normal_text_style))
                main_story.append(Paragraph(f"Description: {proj['Description']}", bullet_text_style))
                main_story.append(Paragraph(f"Technologies: {proj['Technologies']}", bullet_text_style))
                main_story.append(Spacer(1, 8))
            main_story.append(Spacer(1, 12))


        # References Section (matching the image)
        if references:
            main_story.append(Paragraph("References", section_heading))
            for ref in references:
                main_story.append(Paragraph(f"<b>{ref['Name']}</b>", reference_style))
                main_story.append(Paragraph(ref['Title'], reference_style))
                main_story.append(Paragraph(ref['Contact'], reference_style))
                main_story.append(Spacer(1, 8))
            main_story.append(Spacer(1, 12))
        else:
             main_story.append(Paragraph("References available upon request", reference_style))
             main_story.append(Spacer(1, 12))


        # Build the main story which will flow into the main content frame
        doc.build(main_story)

        print(f"Resume saved as '{filename}'")
    except Exception as e:
        print(f"Error generating PDF: {e}")


        
# --- Main execution functions ---
def generate_resumee():
    print("=== Resume Builder ===")

    # Collect data
    personal_info = collect_personal_info()
    education = collect_education()
    experience = collect_experience()
    skills = collect_skills()
    projects = collect_projects() # Keeping projects, as it's useful
    references = collect_references() # Collect references
    e=input("Do you want to generate resume in design format(yes/no)?")
    if e == "yes":
    # Generate PDF
     generate_pdf_resume1(personal_info, education, experience, skills, projects, references)
    else:
        print("Exitting Succesfully!!!!")
        
                            
def resfn():
    generate_resumee()
    print("\nWould you like to generate another resume? (yes/no)")
    if input().lower() == "yes":
        resfn()

if __name__ == "__main__":
    resfn()
