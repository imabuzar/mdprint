from flask import Flask, render_template, request, send_file
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import re
from io import BytesIO

app = Flask(__name__)

# Generating font_config from weasyprint.text.fonts
font_config = FontConfiguration()

# CSS for including Google fonts
font_families_css = CSS(
    "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
    font_config=font_config,
)

# Include Page number CSS
page_number_css = CSS(
    string="""
@page {
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-size: 10pt;
  }
}
"""
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "GET":
        return render_template("generate.html")

    elif request.method == "POST":
        # Getting request data
        data = request.json

        markdown_string = data.get("markdown")
        display_page_number = data.get("display_page_number")
        theme = data.get("theme", "light")

        # Handling CSS Styles
        stylesheets = [font_families_css]
        stylesheets.append(f"static/css/pdf-css/{theme}.css")
        if display_page_number:
            stylesheets.append(page_number_css)

        # Processing Custom Markdown
        markdown_string = process_markdown(markdown_string)
        # Converting Markdown to HTML
        html_string = markdown.markdown(markdown_string)

        # Generating PDF from HTML
        pdf_io = generate_pdf(html_string, stylesheets)
        return send_file(pdf_io, mimetype="application/pdf")


def generate_pdf(html_string: str, stylesheets):
    html = HTML(string=html_string)  # Creating HTML object from weasyprint
    pdf_data = html.write_pdf(
        stylesheets=stylesheets, font_config=font_config
    )  # Writing PDF file

    pdf_io = BytesIO(pdf_data)
    return pdf_io


def process_markdown(markdown_string: str):
    # Page break
    markdown_string = re.sub(
        r"\[page-break\]",
        '<div class="page-break"></div>',
        markdown_string,
    )

    # Cover title
    markdown_string = re.sub(
        r"\[cover-title\](.*?)\[cover-title\]",  # What to replace
        replace_cover_title,  # Replace with (using custom)
        markdown_string,  # Original string
        flags=re.DOTALL,  # allow newlines
    )

    # Section title
    markdown_string = re.sub(
        r"\[section-title\](.*?)\[section-title\]",
        r'<div class="section-page"><h2>\1</h2></div>',
        markdown_string,
    )

    return markdown_string


def replace_cover_title(match):
    # function for re.sub
    content = match.group(1)
    html_content = markdown.markdown(content)
    return f'<div class="cover-page">{html_content}</div>'


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
