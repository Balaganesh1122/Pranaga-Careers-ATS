from app.ai.parser.parser_service import ParserService

text = ParserService.extract_resume_text(
    "uploads/12f84e87-8ed4-4526-9b00-99bded6fbae2.pdf"
)

print("\n========== RESUME TEXT ==========\n")
print(text)