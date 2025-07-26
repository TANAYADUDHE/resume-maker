from fpdf import FPDF
import os

def collect_input(prompt):
    return input(prompt).strip()

def main():
    print("🔹 Welcome to Terminal Resume Generator 🔹\n")

    # Collect user details
    name = collect_input("Full Name: ")
    email = collect_input("Email: ")
    phone = collect_input("Phone Number: ")
    linkedin = collect_input("LinkedIn URL: ")
    github = collect_input("GitHub URL: ")

    print("\n--- Summary Section ---")
    summary = collect_input("Professional Summary: ")

    print("\n--- Education Section ---")
    education = collect_input("Education: ")

    print("\n--- Experience Section ---")
    experience = collect_input("Work Experience: ")

    print("\n--- Skills Section ---")
    skills = collect_input("List your skills (comma separated): ")

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"Email: {email} | Phone: {phone}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"LinkedIn: {linkedin} | GitHub: {github}", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, summary)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Education", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, education)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, experience)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    for skill in skills.split(','):
        pdf.cell(40, 10, f"- {skill.strip()}", ln=True)

    # Save the PDF
    if not os.path.exists("output"):
        os.makedirs("output")

    pdf.output("output/resume.pdf")
    print("\n✅ Resume created successfully: output/resume.pdf")

if __name__ == "__main__":
    main()
