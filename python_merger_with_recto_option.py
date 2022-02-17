import os
import sys
import PyPDF2
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader


#Current dir_path where the script is executed
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print()

combined_file_name = 'combined.pdf'

writer_output = PdfFileWriter()
    
def mergePDF(p_blank_page):
    #check if a 'combined.pdf' file already exist if so, rename it
    if os.path.isfile(combined_file_name):
        os.rename(combined_file_name, 'old_' + combined_file_name)
        print('A combined file has been renamed')
        
    #Add pdf files in an array[]
    pdfs = [file for file in os.listdir(dir_path) if file.endswith('pdf')]

    for pdf in pdfs:
        #Reading the file
        reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
        print('number of pages in: \'', pdf, '\' is: ', reader.numPages)
        
        for page in range(reader.numPages):
            #Add every page in the output
            writer_output.addPage(reader.getPage(page))
        
        #Add a blank page if the number of page is odd
        if (p_blank_page == 't' or p_blank_page == 'true') and reader.numPages % 2 != 0:
            print('adding a blank page')
            writer_output.addBlankPage()
            
    #Writing the final file
    writer_output.write(open(combined_file_name, 'wb'))


#Asking user for param p_blank_page
p_blank_page = input("Always start on recto? (true/false) : ")
mergePDF(p_blank_page)
print('pdfs merged')
os.system("pause")