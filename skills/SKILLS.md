---
name: pdf-processing
description: Extracts text from PDF files using PyPDF2.
---

# PDF Processing Skill

## When to use this skill
Use this skill when a user needs to extract text from a PDF file.

## How to Use this Skill
This skill provides the `extract_text()` function from the `parse_pdf.py` script. Import it into your agent script:

python
from skills.pdf_parsing.parse_pdf import extract_text

result = extract_text(
    file_path="/path/to/document.pdf",
    pages="all"  # or "1-3" or "1,2,3"
)

### Parameters
- `file_path` (str): Path to the PDF file
- `pages` (str): Pages to extract - "all", "1-3" (range), or "1,2,3" (specific pages)

### Returns
JSON object with:
- `success` (bool): Whether extraction succeeded
- `file_path` (str): Path to the processed file
- `total_pages` (int): Total pages in PDF
- `extracted_pages` (int): Number of pages extracted
- `pages` (list): Array of {page: number, text: string} objects

Alternatively, you can call the script directly from the command line:
command
uv run ./skills/pdf-parsing/parse_pdf.py extract_text --file_path /path/to/file.pdf --pages all
