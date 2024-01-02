from pdf2image import convert_from_path
from PIL import Image

def pdf_to_images(pdf_path, image_prefix, format='JPEG', dpi=300):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path, dpi=dpi)

    # Save each image to the specified format
    for i, image in enumerate(images):
        image.save(f"{image_prefix}_page_{i+1}.{format.lower()}", format=format)

# Example usage
pdf_to_images('../sindhi.pdf', 'output', format='JPEG')
