import google.generativeai as genai
import os
from dotenv import load_dotenv
from . import main
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
API_KEY: str = os.getenv("API_KEY")


def prompt():
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-pro')
    # Get the path of the current script
    current_script_path = os.path.abspath(__file__)

    # Construct the path to 'input.pdf' based on the current script path
    pdf_path = os.path.join(os.path.dirname(current_script_path), '..', 'input.pdf')

    text = main.pdf_to_text(pdf_path)
    response = model.generate_content(f"Summarize in bulit points {text} ")
    return response.text


text = prompt()
print(text)
