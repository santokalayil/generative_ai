import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from ..env_variables import get_variable


# def get():
#     # get api key from gemini's website: https://aistudio.google.com/app/apikey
#     genai.configure(api_key=get_variable("GEMINI_API_KEY"))
#     return genai


def get(**kwargs):
    return ChatGoogleGenerativeAI(
        model="gemini-pro",
        verbose=kwargs["verbose"] if "verbose" in kwargs else True,
        temperature=kwargs["temperature"] if "temperature" in kwargs else 0.5,
        google_api_key=get_variable("GEMINI_API_KEY"),
    )
