from pathlib import Path

import pytest

from src.document_loader import load_pdf_text


def test_load_pdf_text_rejects_missing_file():
    missing_file = Path("data/does_not_exist.pdf")

    with pytest.raises(FileNotFoundError):
        load_pdf_text(missing_file)


def test_load_pdf_text_rejects_non_pdf_file(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("This is not a PDF.")

    with pytest.raises(ValueError, match="File must be a PDF"):
        load_pdf_text(text_file)