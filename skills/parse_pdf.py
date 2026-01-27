# /// script
# requires-python = ">=3.12<3.13"
# dependencies = [
#     "pypdf2~=3.0.0",
# ]
# ///

"""
PDF Text Extraction Script

# Originally from:
# https://github.com/adugan-do/Agent-Skills/blob/8e973452a79966aa503bdb65860c0477a62afd1a/skills/pdf-parsing/parse_pdf.py
# Modified to use `uv`.

Extracts text from PDF files using PyPDF2.
Returns JSON output for agent consumption.
"""

import argparse
import json
import sys


def extract_text(file_path: str, pages: str = 'all') -> dict:
    """Extract text from PDF file."""
    try:
        # Try to import PyPDF2
        try:
            import PyPDF2
        except ImportError:
            return {
                'success': False,
                'error': 'PyPDF2 not installed. Run: pip install PyPDF2',
            }

        # Open and read the PDF
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            # Determine which pages to extract
            if pages == 'all':
                page_range = range(num_pages)
            else:
                # Parse page numbers (e.g., "1,2,3" or "1-3")
                page_range = parse_page_range(pages, num_pages)

            # Extract text from specified pages
            extracted_text = []
            for page_num in page_range:
                if 0 <= page_num < num_pages:
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    extracted_text.append({'page': page_num + 1, 'text': text})

            return {
                'success': True,
                'file_path': file_path,
                'total_pages': num_pages,
                'extracted_pages': len(extracted_text),
                'pages': extracted_text,
            }

    except FileNotFoundError:
        return {'success': False, 'error': f'File not found: {file_path}'}
    except Exception as e:
        return {'success': False, 'error': f'Error extracting text: {str(e)}'}


def parse_page_range(pages_str: str, max_pages: int) -> list:
    """Parse page range string into list of page indices."""
    page_indices = []

    # Handle comma-separated pages: "1,2,3"
    if ',' in pages_str:
        for page in pages_str.split(','):
            page_indices.append(int(page.strip()) - 1)
    # Handle range: "1-5"
    elif '-' in pages_str:
        start, end = pages_str.split('-')
        page_indices = list(range(int(start) - 1, int(end)))
    # Single page
    else:
        page_indices = [int(pages_str) - 1]

    return page_indices


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description='Extract text from PDF')
    parser.add_argument('action', help='Action to perform (extract_text)')
    parser.add_argument('--file_path', required=True, help='Path to PDF file')
    parser.add_argument('--pages', default='all', help='Pages to extract (all, 1-3, or 1,2,3)')

    args = parser.parse_args()

    if args.action == 'extract_text':
        result = extract_text(args.file_path, args.pages)
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps({'success': False, 'error': f'Unknown action: {args.action}'}))
        sys.exit(1)


if __name__ == '__main__':
    main()
