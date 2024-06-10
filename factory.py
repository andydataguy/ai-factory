import yaml
from agents.base_agent import BaseAgent
from agents.openai_chat import OpenAIChat, OpenAIConfig

def load_config(config_path: str):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_llm(config, provider: str, model: str) -> BaseAgent:
    llm_config = config['llms']['options'][provider]['models'][model]
    if provider == 'openai_chat':
        return OpenAIChat(OpenAIConfig(**llm_config))
    else:
        raise ValueError(f"Unknown provider: {provider}")
