import os
load_dotenv(override=True, dotenv_path="../.env")
from dotenv import load_dotenv
import requests
r = requests.get("https://monogpt.kr/api/monorouter/v1/credits",
                 headers={"Authorization": f"Bearer {os.getenv('LLM_API_KEY')}"})
print(r.json())