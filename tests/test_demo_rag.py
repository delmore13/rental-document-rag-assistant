import pytest

from app.demo_rag import run_demo


def test_run_demo_rejects_missing_pdf():
    with pytest.raises(FileNotFoundError):
        run_demo("data/does_not_exist.pdf", "What does this say about pets?")