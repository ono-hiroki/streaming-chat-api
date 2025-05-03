from dependency_injector import containers, providers
from app.infrastructure.adapters.openai_client import OpenAIClient
from app.use_cases.chat_stream_action import ChatStreamAction
from openai import OpenAI


class ApplicationContainer(containers.DeclarativeContainer):
    openai_client = providers.Singleton(OpenAI)
    openai_client_adapter = providers.Singleton(OpenAIClient, client=openai_client)
    chat_stream_action = providers.Factory(ChatStreamAction, openai_client=openai_client_adapter)
