from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
