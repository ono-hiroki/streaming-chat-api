import json
from typing import List, Dict, Generator
from openai import OpenAI

from app.domain.adapters.openai_client_interface import IOpenAIClient


class OpenAIClient(IOpenAIClient):
    def __init__(self, client: OpenAI, model: str = "gpt-4o-mini"):
        self.client = client
        self.model = model

    def stream_chat(self, messages: List[Dict[str, str]]) -> Generator[str, None, None]:
        """
        OpenAI からのストリーミング応答を SSE 形式で yield する。
        """
        response = self.client.chat.completions.create(
            model=self.model, stream=True, messages=messages
        )
        for chunk in response:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                yield f"data: {delta.content}\n\n"
        yield "event: done\ndata: [DONE]\n\n"