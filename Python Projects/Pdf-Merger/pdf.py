import PyPDF2
from sys import argv

inputs = argv[1:]

def pdf_merger(pdf_files):
	merger = PyPDF2.PdfFileMerger(pdf_files)
	for pdf in pdf_files:
		print(pdf)
		merger.append(pdf)
	merger.write('merged_pdf.pdf')


pdf_merger(inputs)
