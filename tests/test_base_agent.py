import pytest
from agents.base_agent import BaseAgent

class DummyAgent(BaseAgent):
    def generate(self, prompt: str) -> str:
        return f"Response: {prompt}"

def test_generate():
    agent = DummyAgent()
    prompt = "Hello"
    assert agent.generate(prompt) == "Response: Hello"
