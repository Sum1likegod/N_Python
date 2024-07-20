import os as o
import PyPDF2 as p

all_files = o.listdir()
changes = p.PdfWriter()
all_pdfs = [x for x in all_files if x.endswith(".pdf")]
for i in all_pdfs:
  changes.append(i)

print("Operation Successful")
changes.write("new_merged_pdf.pdf")
changes.close()

