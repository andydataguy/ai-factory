import yaml
from factory import load_config, get_llm

def main():
    # Load configuration
    config_path = 'config/config.yaml'
    config = load_config(config_path)

    # Instantiate components
    provider = 'openai_chat'
    model = 'fast_model'
    llm = get_llm(config, provider, model)

    # Generate content
    prompt = "Tell me a joke about programming."
    results = llm.generate(prompt)
    print(results)

if __name__ == "__main__":
    main()
