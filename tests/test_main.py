import pytest
from src import main


def test_pdf_to_text():
    # Define paths for a sample PDF

    # Call the function to convert PDF to text
    result_text = main.pdf_to_text('../input.pdf')

    # Assert that the result is not an empty string
    assert result_text.strip()  # This will raise an error if the string is empty
