# #create Node
# from collections import deque
# class Node :
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None
    
# def createTree(l1):
#     if len(l1)==0 :
#         return None
#     else :
#         root=Node(l1[0])
#         d1=deque()
#         d1.append(root)
#         i=1
#         while len(l1)>i:
#          if l1[i]!=None :
#             if i%2==0 :
#                 n1=Node(l1[i])
#                 d1[0].right=n1
#                 d1.append(n1)
#                 d1.popleft()
#             else :
#                 n1=Node(l1[i])
#                 d1[0].left=n1
#                 d1.append(n1)
#          i+=1
#     return root





# root=createTree([1,2,3,None,4,None,5])

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm

# Create document with tight margins (important)
doc = SimpleDocTemplate(
    "salary_slip_exact_clone.pdf",
    pagesize=A4,
    leftMargin=15,
    rightMargin=15,
    topMargin=15,
    bottomMargin=15
)

elements = []

# ----------- CUSTOM STYLES -----------
title_style = ParagraphStyle(
    name='TitleStyle',
    fontName='Helvetica-Bold',
    fontSize=14,
    alignment=1,  # center
    spaceAfter=6
)

sub_style = ParagraphStyle(
    name='SubStyle',
    fontName='Helvetica',
    fontSize=9,
    alignment=1
)

normal_style = ParagraphStyle(
    name='NormalStyle',
    fontName='Helvetica',
    fontSize=9
)

bold_style = ParagraphStyle(
    name='BoldStyle',
    fontName='Helvetica-Bold',
    fontSize=9
)

# ----------- HEADER -----------
elements.append(Paragraph("A complete web enabled Education Administration Software", sub_style))
elements.append(Spacer(1, 6))
elements.append(Paragraph("SALARY SLIP - MARCH 2026", title_style))
elements.append(Spacer(1, 10))

# ----------- EMPLOYEE INFO BOX -----------
emp_data = [
    ["Employee Name", "Nandan Mishra", "Employee ID", "EMP001"],
    ["Department", "IT", "Designation", "Software Engineer"],
    ["Month", "March 2026", "Working Days", "30"],
]

emp_table = Table(emp_data, colWidths=[70, 120, 70, 120])
emp_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
elements.append(emp_table)
elements.append(Spacer(1, 12))

# ----------- SALARY TABLE -----------
salary_data = [
    ["EARNINGS", "AMOUNT (₹)", "DEDUCTIONS", "AMOUNT (₹)"],
    ["Basic Salary", "30000", "PF", "2000"],
    ["HRA", "10000", "Professional Tax", "1500"],
    ["Bonus", "5000", "Other Deduction", "500"],
    ["", "", "", ""],
    ["TOTAL", "45000", "TOTAL", "4000"],
]

salary_table = Table(salary_data, colWidths=[90, 80, 90, 80])

salary_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),

    # Header
    ('BACKGROUND', (0,0), (-1,0), colors.black),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),

    # Alignment
    ('ALIGN', (1,1), (1,-1), 'RIGHT'),
    ('ALIGN', (3,1), (3,-1), 'RIGHT'),

    # TOTAL bold
    ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),

    # Tight padding like original
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
elements.append(salary_table)
elements.append(Spacer(1, 12))

# ----------- NET SALARY BOX -----------
net_table = Table(
    [["Net Salary (₹)", "41000"]],
    colWidths=[170, 170]
)

net_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1.2, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ('ALIGN', (1,0), (1,0), 'RIGHT'),
    ('BACKGROUND', (0,0), (-1,-1), colors.lightgrey),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
elements.append(net_table)

elements.append(Spacer(1, 20))

# ----------- FOOTER -----------
elements.append(Paragraph("This is a system generated salary slip.", normal_style))

# BUILD
doc.build(elements)

print("Pixel-accurate salary slip generated.")