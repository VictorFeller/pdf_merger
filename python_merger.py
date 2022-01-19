import os
from PyPDF2 import PdfFileMerger

#Current dir_path where the script is executed
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#Add pdf files in an array[]
pdfs = [file for file in os.listdir(dir_path) if file.endswith('pdf')]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("combined.pdf")
merger.close()
#os.system("pause")
