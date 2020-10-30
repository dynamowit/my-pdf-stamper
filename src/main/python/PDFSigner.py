import PyPDF2
import os
import fitz

def signPDF(pngPath, pdfsFolder):
    print("Stamping Started......")

    for filename in os.listdir(pdfsFolder):
        if filename.endswith(".pdf"):
            print("Start prcessing "+os.path.join(pdfsFolder, filename)+" ......")
            file_handle = fitz.open(os.path.join(pdfsFolder, filename))
            first_page = file_handle[0]

            first_page.insertImage(fitz.Rect(450,20,550,120), pngPath)
            file_handle.save(os.path.join(pdfsFolder, "signed-"+filename))
           # with open(os.path.join(pdfsFolder, filename), "rb") as filehandle_input:

           #     pdf = PyPDF2.PdfFileReader(filehandle_input)
                                      
                #hoping to loop all pages                        
           #     first_page = pdf.getPage(0)  
           #     
                    
                                        
           #     pdf_writer = PyPDF2.PdfFileWriter()                        
           #     pdf_writer.addPage(first_page)
                
            #    with open(os.path.join(pdfsFolder, "signed-"+filename), "wb") as filehandle_output: 
            #        pdf_writer.write(filehandle_output)
            print("Done prcessing "+os.path.join(pdfsFolder, filename)+" ......")
        else:
            continue
