# MDPrint

A web application built with Python Flask for generating PDF documents from Markdown.

## Features

- Generate professional-looking PDF documents from Markdown.
- Customize your PDFs with various themes and options for page numbers.
- Effortlessly create and download your PDF documents.

## Getting Started

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- WeasyPrint
- Markdown

### Installation

1. Clone the repository:  
   `git clone https://github.com/imabuzar/mdprint.git`
2. Navigate to the project directory:  
   `cd mdprint`
3. Create a virtual environment:
   - On **Windows**:  
     `python -m venv .venv`
   - On **macOS/Linux**:  
     `python3 -m venv .venv`
4. Activate the virtual environment:
   - On **Windows**:  
     `.\.venv\Scripts\activate`
   - On **macOS/Linux**:  
     `source .venv/bin/activate`
5. Install the dependencies:  
   `pip install -r requirements.txt`
6. Run the application:  
   `flask run`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Click on the "Generate PDF Now" button to access the Markdown editor.
3. Write your Markdown content and customize your PDF settings.
4. Click the "Generate PDF" button to download your PDF document.

## Customization

### Themes

MDPrint comes with two built-in themes: Light and Dark. You can switch between these themes in the Markdown editor.

### Page Numbers

Choose to display page numbers in your PDF document. This option is available in the Markdown editor.

## Markdown Syntax

MDPrint uses standard Markdown syntax. You can create content using headings, paragraphs, lists, links, images, and more.

### Custom Markdown Elements

MDPrint supports the following custom Markdown elements:

- `[cover-title]`: Creates a cover title page.
- `[section-title]`: Creates a section title page.
- `[page-break]`: Inserts a page break.

## Contributing

Contributions are welcome! If you'd like to contribute to MDPrint, please fork the repository and submit a pull request.

## License

MDPrint is licensed under the MIT License.

## Acknowledgments

- [WeasyPrint](https://weasyprint.org/) for generating PDF documents.
- [Markdown](https://www.markdownguide.org/) for parsing Markdown content.
- [Flask](https://flask.palletsprojects.com/) for building the web application.
