import sys
from pathlib import Path

# 상위 폴더의 common_config.py를 불러오기 위해 경로 추가 (어느 폴더에서 실행해도 동작)
sys.path.append(str(Path(__file__).resolve().parent.parent))

from langchain.agents import create_agent
from common_config import llm_connect


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = llm_connect()

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
)

# .py 스크립트는 노트북과 달리 print()를 해야 결과가 보임
print(result)                            # 딕셔너리 전체 (질문, 도구 호출, 도구 결과, 최종 답변)
# print(result["messages"][-1].content)  # 최종 답변 문장만 보고 싶을 때