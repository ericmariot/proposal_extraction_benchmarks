from extractors.py_mupdf import PyMuPDFExtractor
from extractors.pdf_plumber import PdfPlumberExtractor
from extractors.py_pdfium2 import PyPdfium2Extractor
from instructions.geico import GEICO_INSTRUCTIONS
from instructions.progressive import PROGRESSIVE_INSTRUCTIONS


class PdfExtractor:
    PYMUPDF = "py_mupdf"
    PDFPLUMBER = "pdf_plumber"
    PYPDFIUM = "py_pdfium2"


class Carrier:
    PROGRESSIVE = "progressive"
    GEICO = "geico"


EXTRACTORS = {
    PdfExtractor.PYMUPDF: PyMuPDFExtractor(),
    PdfExtractor.PDFPLUMBER: PdfPlumberExtractor(),
    PdfExtractor.PYPDFIUM: PyPdfium2Extractor(),
}

INSTRUCTIONS = {
    Carrier.PROGRESSIVE: PROGRESSIVE_INSTRUCTIONS,
    Carrier.GEICO: GEICO_INSTRUCTIONS,
}

MODES = {
    "single": "Extract with one extractor + optional OpenAI",
    "benchmark": "Benchmark all extractors (no OpenAI)",
}
