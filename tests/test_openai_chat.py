import pytest

def test_generate(openai_chat):
    prompt = "Tell me a joke about programming."
    response = openai_chat.generate(prompt)
    assert response == "Hello, world!"
