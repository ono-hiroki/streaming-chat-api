from typing import List, Dict, Generator, Protocol

class IOpenAIClient(Protocol):
    def stream_chat(self, messages: List[Dict[str, str]]) -> Generator[str, None, None]:
        """
        OpenAI からのストリーミング応答を SSE 形式で yield する。
        """
        ...