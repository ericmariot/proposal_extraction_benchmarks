from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, pdf_bytes: bytes) -> list[dict]:
        pass
