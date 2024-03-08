from ..utils.huggingface import get_llm


def get(**kwargs):
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    model_kwargs = kwargs if kwargs else {"temperature": 0.5, "max_tokens": 4096}
    return get_llm(repo_id, model_kwargs)
