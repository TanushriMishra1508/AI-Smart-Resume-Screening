import pdfplumber
import PyPDF2


def extract_text(uploaded_file):
    """
    Extract text from a PDF resume.
    First tries pdfplumber, then falls back to PyPDF2.
    """

    text = ""

    try:
        uploaded_file.seek(0)

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception:

        try:
            uploaded_file.seek(0)

            reader = PyPDF2.PdfReader(uploaded_file)

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        except Exception:
            text = ""

    return text