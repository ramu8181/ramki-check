from pdf2docx import Converter
import aspose.slides as slides

# Create presentation

def create_presentations(file1,file2):

    with slides.Presentation() as pres:

       # Remove default slide from presentation
       pres.slides.remove_at(0)
       # Import PDF to presentation
       pres.slides.add_from_pdf(file1)
       # Save presentation
       pres.save("pdf-to-ppt.pptx", slides.export.SaveFormat.PPTX)


def convert_doc(file1, file2):
   
   cv = Converter(pdf_file)
   cv.convert(docx_file)
   cv.close()


if __name__=='__main__':
    pdf_file = 'BRKMPL-2130.pdf'
    docx_file = 'sample11.pptx'
    create_presentations(pdf_file,docx_file)
