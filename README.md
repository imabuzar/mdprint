# MDPrint

A web application built with Python Flask for generating PDF documents from Markdown.

## Features

- Generate professional-looking PDF documents from Markdown.
- Customize your PDFs with various themes and options for page numbers.
- Effortlessly create and download your PDF documents.

## Getting Started

### Prerequisites

- Docker (for Docker installation)
- Python 3.12 or higher (for non-Docker installation)

### Installation

**Note:** We recommend using the Docker installation method, as `weasyprint` relies on certain system packages that can be challenging to install manually.

### From Docker (Recommended)

1. Pull the Docker image from Docker Hub:  
   `docker pull imabuzar/mdprint`
2. Run the Docker container:  
   `docker run -it -p 5000:5000 imabuzar/mdprint`

### From Github

1. Clone the repository:  
   `git clone https://github.com/imabuzar/mdprint.git`
2. Navigate to the project directory:  
   `cd mdprint`
3. Create a virtual environment:
   `python3 -m venv .venv` (on Linux/Mac) or `python -m venv .venv` (on Windows)
4. Activate the virtual environment:
   `source .venv/bin/activate` (on Linux/Mac) or `.venv\Scripts\activate` (on Windows)
5. Install the dependencies:  
   `pip install -r requirements.txt`
6. Run the application:  
   `flask run`

## Usage

1. Open your web browser and navigate to `http://localhost:5000` (or custom port if using docker).
2. Write your Markdown content, generate and download PDF document.

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
