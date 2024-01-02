import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (replace '/usr/bin/tesseract' with the actual path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def jpeg_to_text(image_path):
    # Open the JPEG image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Example usage
result_text = jpeg_to_text('output_page_4.jpeg')
print(result_text)
