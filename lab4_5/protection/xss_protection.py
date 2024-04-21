import html


class XSSProtection:
    @staticmethod
    def escape_html(input_text):
        return html.escape(input_text)