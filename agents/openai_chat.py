import os
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError
from dotenv import load_dotenv
from .base_agent import BaseAgent

load_dotenv()

class OpenAIConfig(BaseModel):
    model: str
    max_history_words: int
    max_words_per_message: int
    stream: bool
    max_retry: int

class OpenAIChat(BaseAgent):
    def __init__(self, config: OpenAIConfig):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = config.model
        self.max_history_words = config.max_history_words
        self.max_words_per_message = config.max_words_per_message
        self.stream = config.stream
        self.max_retry = config.max_retry
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=self.max_words_per_message,
            stream=self.stream
        )

        if self.stream: 
            assistant_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    text_chunk = chunk.choices[0].delta.content
                    assistant_response += str(text_chunk)
            return assistant_response.strip()
        else:
            return response.choices[0].message.content
