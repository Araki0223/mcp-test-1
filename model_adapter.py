from openai import OpenAI
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # 環境変数で管理

def call_openai(messages: List[Dict], temperature: float = 0.7) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
