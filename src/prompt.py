import google.generativeai as genai
import os
from dotenv import load_dotenv
from . import main
from . import pdfimagetotext
# import main
# import pdfimagetotext

load_dotenv()
API_KEY: str = os.getenv("API_KEY")


def remove_lines_with_www(text):
    """
    Removes lines from the given text that contain the substring "www."

    Parameters:
        text (str): The input text to process.

    Returns:
        str: The processed text with lines containing "www." removed.
    """
    # Split the text into lines
    lines = text.split('\n')

    # Remove lines containing "www."
    filtered_lines = [line for line in lines if "www." not in line]

    # Concatenate the remaining lines into a single string
    result_text = '\n'.join(filtered_lines)

    return result_text


def prompt():
    """
    Initializes the prompt function.

    Returns:
        str: The generated content from the model.
    """
    # now this will convert the pdf to text if that does not work then i will convert the images theb to text
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-pro')
    # Get the path of the current script
    current_script_path = os.path.abspath(__file__)

    # Construct the path to 'input.pdf' based on the current script path
    pdf_path = os.path.join(os.path.dirname(
        current_script_path), '..', 'input1.pdf')

    result = main.pdf_to_text(pdf_path)
    text = remove_lines_with_www(result)

    if text is None or len(text) <= 10:
        text = pdfimagetotext.pdf_images_to_text(pdf_path)
    # Following prompt is not working
    prompt = f"""
    Suppose you are examiner for School student  and are going to take a test so you have to  generate a set of 10 multiple-choice questions MCQs.
    Each question should include 4 answer options with options like a ,b ,c,d those options should be related to the same topic and just one should be right answer,
    and please provide the correct answer for each question along with a shortest explanation.
    Please ensure that the questions cover various topic in given {text}.
    """
    response = model.generate_content(prompt)
    return response.text


text = prompt()
print(text)
