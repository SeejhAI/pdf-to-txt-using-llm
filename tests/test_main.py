from src import main
import os


def test_pdf_to_text():
    current_script_path = os.path.abspath(__file__)
    # Define paths for a sample PDF
    pdf_path = os.path.join(os.path.dirname(
        current_script_path), '..', 'input.pdf')
    # Call the function to convert PDF to text
    result_text = main.pdf_to_text(pdf_path)

    # Assert that the result is not an empty string
    assert result_text.strip()  # This will raise an error if the string is empty
