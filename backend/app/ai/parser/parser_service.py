import os

from app.ai.parser.pdf_parser import PDFParser
from app.ai.parser.docx_parser import DOCXParser


class ParserService:

    @staticmethod
    def extract_resume_text(file_path: str):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return PDFParser.extract_text(file_path)

        elif extension == ".docx":
            return DOCXParser.extract_text(file_path)

        raise ValueError("Unsupported file format")