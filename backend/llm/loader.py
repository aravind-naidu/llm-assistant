from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_models.huggingface import ChatHuggingFace

def get_llm(provider: str = "ollama"):
    if provider == "ollama":
        return ChatOllama(model="llama3.1:8b", temperature=0.3)
    elif provider == "huggingface":
        return ChatHuggingFace(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
    elif provider == "openai":
        return ChatOpenAI(model_name="gpt-4", temperature=0.3)
    else:
        raise ValueError(f"Unknown provider: {provider}")
