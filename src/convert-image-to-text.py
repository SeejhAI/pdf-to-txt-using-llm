import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (replace '/usr/bin/tesseract' with the actual path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def jpeg_to_text(image_path):
    """
    Convert a JPEG image to text using optical character recognition (OCR).

    Args:
        image_path (str): The path to the JPEG image file.

    Returns:
        str: The extracted text from the image.
    """
    # Open the JPEG image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage
result_text = jpeg_to_text('output_page_4.jpeg')
print(result_text)
