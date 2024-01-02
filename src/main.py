import pypdf


def pdf_to_text(pdf_path):
    """
    Convert a PDF file to text.

    Parameters:
    pdf_path (str): The path of the PDF file.

    Returns:
    str: The extracted text from the PDF file.
    """
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = pypdf.PdfReader(pdf_file)
        # Initialize an empty string to store the text
        text = ""
        # Iterate through all pages and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text
