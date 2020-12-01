      # install pip-pymuPDF, first, to activate , fitz,

# PYTHON DEEP LEARNING- Extracting  text from PDF pages - PDF Handling 

import fitz

pdf = fitz.open("RetireYoungRetireRich.pdf")
print(pdf.pageCount)

page = pdf.loadPage(27)
text = page.getText("text")
#print(text)  # no spacing
print(text.replace("\t","")) # space between lines enabler

"""
HOW TO SAVE AS NOTEPAD FILE: 
with open("pypage17.txt","w")as file:
    file.write(text.replace("\t",""))
"""

pdf.close()
