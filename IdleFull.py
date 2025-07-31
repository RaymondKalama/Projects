from fpdf import FPDF

# Create a PDF class for the visual one-pager
class OnboardingGuidePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 70, 127)
        self.cell(0, 10, "Idle Full Officer - Onboarding Guide", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, text):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, text)
        self.ln()

# Create the PDF
pdf = OnboardingGuidePDF()
pdf.add_page()

# Role Overview
pdf.section_title("🧭 Role Overview")
pdf.section_body(
    "As an Idle Full Officer, your mission is to manage idle full containers—those that remain stationary for extended periods. "
    "You ensure these containers are returned, invoiced, or escalated to avoid financial and legal risks."
)

# Key Responsibilities
pdf.section_title("🛠️ Key Responsibilities")
pdf.section_body(
    "1. Idle Full Container Follow-Up:\n"
    "   - Monitor containers using GAIA, NOVA, LARA.\n"
    "   - Engage clients via email/phone.\n"
    "   - Escalate unresolved cases after 30–40 days.\n"
    "   - Categorize by idle duration and status.\n\n"
    "2. Demurrage & Detention (D&D) Invoicing:\n"
    "   - Generate/send D&D invoices.\n"
    "   - Respond to D&D queries.\n"
    "   - Report weekly to TBI desk.\n\n"
    "3. Reporting & Documentation:\n"
    "   - Submit daily/weekly/monthly reports.\n"
    "   - File waivers for special cases.\n\n"
    "4. Legal & Salvage Coordination:\n"
    "   - Coordinate disposal of unrecoverable containers.\n"
    "   - Prepare legal notices and vendor quotes."
)

# KPIs
pdf.section_title("📊 Key Performance Indicators (KPIs)")
pdf.section_body(
    "- Idle Full Resolution Rate: % resolved within 30–60 days\n"
    "- D&D Invoicing Timeliness: % issued within SLA\n"
    "- Escalation Accuracy: % with complete documentation\n"
    "- Client Response Rate: % responded within 7 days\n"
    "- Reporting Compliance: Timely report submissions\n"
    "- Reduction in Long Idle Cases: Fewer >90-day idle containers"
)

# Tools & Systems
pdf.section_title("🧩 Tools & Systems")
pdf.section_body(
    "- GAIA: Container tracking\n"
    "- LARA & NOVA: Idle chasing, waiver filing\n"
    "- IRIS: Role-based access\n"
    "- Email & Phone: Client/internal communication"
)

# Knowledge Areas
pdf.section_title("🧠 Knowledge Areas")
pdf.section_body(
    "- Import/export laws and regulations\n"
    "- Idle full and D&D SOPs\n"
    "- Escalation protocols\n"
    "- Legal/salvage procedures"
)

# Save the PDF
pdf.output("Idle_Full_Officer_Onboarding_Guide.pdf")