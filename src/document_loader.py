from pathlib import Path
from typing import Union

from pypdf import PdfReader


def load_pdf_text(file_path: Union[str, Path]) -> str:
    """
    Extract text from a PDF file and return it as a single cleaned string.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from all readable pages.

    Raises:
        FileNotFoundError: If the PDF file does not exist.
        ValueError: If the file is not a PDF or no text can be extracted.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("File must be a PDF.")

    reader = PdfReader(str(path))
    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            cleaned_text = " ".join(page_text.split())
            extracted_pages.append(f"[Page {page_number}] {cleaned_text}")

    full_text = "\n\n".join(extracted_pages).strip()

    if not full_text:
        raise ValueError("No readable text could be extracted from this PDF.")

    return full_text


if __name__ == "__main__":
    sample_path = Path("data/sample.pdf")

    try:
        text = load_pdf_text(sample_path)
        print(text[:1000])
    except Exception as error:
        print(f"Error: {error}")