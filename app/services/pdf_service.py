import fitz  # PyMuPDF

def extract_text(pdf_path):
    pdf_document = fitz.open(pdf_path)
    pdf_text = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        pdf_text.append(text)

    return pdf_text
