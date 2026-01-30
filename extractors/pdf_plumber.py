import pdfplumber
from io import BytesIO

from extractors.base import BaseExtractor


class PdfPlumberExtractor(BaseExtractor):
    def extract(self, pdf_bytes: bytes) -> list[dict]:
        pdf = pdfplumber.open(BytesIO(pdf_bytes))

        pages = []
        for i, page in enumerate(pdf.pages, start=1):
            pages.append({"page_number": i, "text": page.extract_text() or ""})

        pdf.close()

        return pages
