from pprint import pprint

from app.ai.parser.parser_service import ParserService
from app.ai.parser.information_extractor import (
    ResumeInformationExtractor,
)

text = ParserService.extract_resume_text(
    "uploads/12f84e87-8ed4-4526-9b00-99bded6fbae2.pdf"
)

result = ResumeInformationExtractor.extract(text)

pprint(result)