import os
import google.generativeai as genai


def get():
    # get api key from gemini's website: https://aistudio.google.com/app/apikey
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai
