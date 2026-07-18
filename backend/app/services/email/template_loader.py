from pathlib import Path


class EmailTemplateLoader:

    # backend/templates
    TEMPLATE_DIR = Path(__file__).resolve().parents[3] / "templates"

    @staticmethod
    def load_template(
        template_name: str,
        context: dict,
    ) -> str:

        template_path = EmailTemplateLoader.TEMPLATE_DIR / template_name

        # Debug (remove later)
        print("Template Directory :", EmailTemplateLoader.TEMPLATE_DIR)
        print("Template Path      :", template_path)
        print("File Exists        :", template_path.exists())

        if not template_path.exists():
            raise FileNotFoundError(
                f"Email template '{template_name}' not found.\n"
                f"Expected path: {template_path}"
            )

        html = template_path.read_text(encoding="utf-8")

        for key, value in context.items():
            html = html.replace(f"{{{{{key}}}}}", str(value))
            html = html.replace(f"{{{{ {key} }}}}", str(value))

        return html