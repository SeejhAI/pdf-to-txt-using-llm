import google.generativeai as genai
import os
from dotenv import load_dotenv
import main
load_dotenv()


DB_URI: str = os.getenv("DB_URI")
API_KEY: str = os.getenv("API_KEY")


def propmt():
    genai.configure(
        api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name='gemini-pro')
    text = main.pdf_to_text('../input.pdf')
    response = model.generate_content(f"Summarize in bulit points {text} ")
    return response.text


text = propmt()
print(text)
