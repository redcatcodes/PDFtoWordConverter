import PyPDF2
import docx

def convert_pdf_to_word(pdf_file_path, word_file_path, pages_to_convert):
    with open(pdf_file_path, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)

        word_document = docx.Document()
        for page in pages_to_convert:
            page_content = reader.getPage(page).extractText()
            paragraph = docx.paragraph.Paragraph(page_content)
            word_document.add_paragraph(paragraph)

    word_document.save(word_file_path)

convert_pdf_to_word('input.pdf', 'output.docx', [1, 2]) 

# This code will create a Word document with ALL the pages of the PDF file.
convert_pdf_to_word('input.pdf', 'output.docx', [])

# Can use the range function also
# This code will create a Word document with the first 10 pages of the PDF file.
convert_pdf_to_word('input.pdf', 'output.docx', range(1, 11)) 

# This code will create a Word document with the first two pages of the PDF file.
convert_pdf_to_word('input.pdf', 'output.docx', [1, 2])

# This will create a Word document with the second page of the PDF file input.pdf.
convert_pdf_to_word('input.pdf', 'output.docx', [2])
