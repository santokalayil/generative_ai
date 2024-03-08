import os

# from langchain_community.llms import HuggingFaceHub
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from ..env_variables import get_variable


def get_llm(repo_id, model_kwargs):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HUGGINGFACEHUB_API_KEY"]
    return HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs=model_kwargs,
    )
