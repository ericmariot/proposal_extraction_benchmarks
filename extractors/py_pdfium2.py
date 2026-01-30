import pypdfium2 as pdfium

from extractors.base import BaseExtractor


class PyPdfium2Extractor(BaseExtractor):
    def extract(self, pdf_bytes: bytes) -> list[dict]:

        pdf = pdfium.PdfDocument(pdf_bytes)
        pages = []

        for i in range(len(pdf)):
            page = pdf[i]
            textpage = page.get_textpage()
            pages.append(
                {"page_number": i + 1, "text": textpage.get_text_bounded() or ""}
            )
        return pages
