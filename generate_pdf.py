from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

file_name = "Rock_Paper_Scissors_Project_Report.pdf"

styles = getSampleStyleSheet()
content = []

title = Paragraph("Rock–Paper–Scissors Game Using Python", styles['Title'])
content.append(title)
content.append(Spacer(1,20))

text = """
Abstract:
This project implements the classic Rock–Paper–Scissors game using Python.
The user plays against the computer and the program determines the winner.

Introduction:
Rock–Paper–Scissors is a simple game played between two players.
In this project the user competes with the computer.

Game Rules:
Rock beats Scissors
Scissors beat Paper
Paper beats Rock

Conclusion:
This project demonstrates Python basics such as loops,
conditions and random number generation.
"""

for line in text.split("\n"):
    content.append(Paragraph(line, styles['BodyText']))
    content.append(Spacer(1,10))

doc = SimpleDocTemplate(file_name, pagesize=A4)
doc.build(content)

print("PDF Generated Successfully!")
