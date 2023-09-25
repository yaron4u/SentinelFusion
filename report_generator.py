# report_generator.py
from reportlab.pdfgen import canvas
import db_manager


def generate_pdf_report(incidents):
    # Function to generate a PDF report
    print("Incidents: ", incidents)
    c = canvas.Canvas("./report.pdf")

    c.setFont("Helvetica", 24)
    c.drawString(100, 800, "Incident Report")

    c.setFont("Helvetica", 12)
    c.drawString(100, 780, "Incidents:")

    status = incidents["status"]
    details = incidents["details"]

    for i, incident in enumerate(incidents):
        # print all incidents valuse in the pdf
        c.drawString(100, 750 - i * 100, "Status: " + status)
        c.drawString(100, 730 - i * 100, "Details: " + details)

    c.save()
