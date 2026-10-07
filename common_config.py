from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
# 모델을 넘겨줌
model = "gpt-5.4-mini"
temperature = 2
max_tokens = 2086

def llm_connect(
    model : str=model,
    api_key: str=api_key,
    base_url: str=base_url,
    temperature: float = temperature,
    max_tokens: int = max_tokens
):
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=base_url,
        temperature=temperature,
        use_responses_api=False,  # base url로 할 때는 이부분 넣어야 함.(MonoRouter 사용)
        max_tokens=max_tokens,
    )

llm = llm_connect(model=model)  # 함수 정의 뒤에 호출해야 함

from langchain_openai import OpenAIEmbeddings

def embedding_model():
    embedding_model = "text-embedding-3-small"
    embeddings = OpenAIEmbeddings(
        model=embedding_model,
        api_key=api_key,
        base_url=base_url,
        # OpenAIEmbeddings에는 use_responses_api 옵션이 없음 (넣으면 TypeError)
    )
    # print(f"Embedding model: {embedding_model}")
    return embeddings