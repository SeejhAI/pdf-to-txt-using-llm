from dotenv import load_dotenv
import os
from src import prompt
load_dotenv()
API_KEY: str = os.getenv("API_KEY")
print(API_KEY)
# from src.prompt import API_KEY










def test_checking_api_key():
    assert API_KEY.strip()  # This will raise an error if the string is empty


def test_checking_prompt():
    pr  = prompt.prompt()
    assert pr.strip()