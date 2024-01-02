from pdf2image import convert_from_path
import pytesseract


# Set the path to the Tesseract executable (replace '/usr/bin/tesseract' with the actual path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def pdf_images_to_text(pdf_path, dpi=300):
    """
    Converts a PDF file to text by extracting text from each page image.

    Parameters:
        pdf_path (str): The path to the PDF file.
        dpi (int): The resolution in dots per inch of the extracted images. Default is 300.

    Returns:
        str: The extracted text from all pages, separated by page numbers.
    """
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path, dpi=dpi)

    # Initialize an empty string to store the text
    all_text = ""

    # Use Tesseract to extract text from each image
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        all_text += f"\n\nPage {i+1}:\n{text}"

    return all_text


# Example usage
if __name__ == '__main__':
    result_text = pdf_images_to_text('../sindhi.pdf')
    print(result_text)
