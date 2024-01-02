from pdf2image import convert_from_path


def pdf_to_images(pdf_path, image_prefix, format='JPEG', dpi=300):
    """
    Convert a PDF file to a list of images.

    Args:
        pdf_path (str): The path to the PDF file.
        image_prefix (str): The prefix to use for each image file.
        format (str, optional): The format to save the images in. Defaults to 'JPEG'.
        dpi (int, optional): The DPI (dots per inch) resolution of the images. Defaults to 300.
    """
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path, dpi=dpi)

    # Save each image to the specified format
    for i, image in enumerate(images):
        image.save(f"{image_prefix}_page_{i+1}.{format.lower()}", format=format)


# Example usage
pdf_to_images('../sindhi.pdf', 'output', format='JPEG')
