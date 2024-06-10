# conftest.py
import pytest
from agents.openai_chat import OpenAIChat, OpenAIConfig

@pytest.fixture
def openai_chat():
    config = OpenAIConfig(
        model='gpt-3.5-turbo',
        max_history_words=10000,
        max_words_per_message=500,
        stream=True,
        max_retry=10
    )
    return OpenAIChat(config)
