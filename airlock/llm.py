import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def chat(system: str, messages: list, tools: list = None):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    model = os.environ.get("MODEL", "claude-haiku-4-5-20251001")

    # If api_key is present, use it, else let the SDK discover auth (e.g. from environment/profile)
    client_kwargs = {}
    if api_key:
        client_kwargs["api_key"] = api_key

    client = anthropic.Anthropic(**client_kwargs)

    kwargs = {
        "model": model,
        "max_tokens": 1024,
        "system": system,
        "messages": messages,
    }

    if tools:
        kwargs["tools"] = tools

    return client.messages.create(**kwargs)
