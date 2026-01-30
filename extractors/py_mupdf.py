import fitz

from extractors.base import BaseExtractor


class PyMuPDFExtractor(BaseExtractor):
    def extract(self, pdf_bytes: bytes) -> list[dict]:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        pages = []
        for i, page in enumerate(doc, start=1):
            pages.append({"page_number": i, "text": page.get_text() or ""})
        doc.close()

        return pages
