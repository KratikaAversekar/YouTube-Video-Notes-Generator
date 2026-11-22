#pdf_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from xml.sax.saxutils import escape
from io import BytesIO


def create_pdf(notes):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        textColor=colors.darkblue,
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = styles["BodyText"]
    story = []

    story.append(
        Paragraph("YOUTUBE VIDEO NOTES", title_style)
    )

    story.append(Spacer(1, 0.2 * inch))

    for line in notes.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        safe_line = escape(line)

        if line.startswith("🔹"):
            story.append(
                Paragraph(safe_line, heading_style)
            )

        elif line.startswith("•"):
            story.append(
                Paragraph(safe_line, body_style)
            )

        elif line.startswith("📘"):
            continue

        elif line.startswith("="):
            continue

        else:
            story.append(
                Paragraph(safe_line, body_style)
            )

    doc.build(story)

    buffer.seek(0)

    return buffer.getvalue()
