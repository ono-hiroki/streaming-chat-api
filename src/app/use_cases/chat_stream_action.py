from typing import List, Dict, Generator
from app.infrastructure.adapters.openai_client import OpenAIClient

class ChatStreamAction:
    def __init__(self, openai_client: OpenAIClient):
        self.openai_client = openai_client

    def execute(self, messages: List[Dict[str, str]]) -> Generator[str, None, None]:
        return self.openai_client.stream_chat(messages)