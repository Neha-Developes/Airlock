"""Thin wrapper around OpenAI-compatible chat endpoints (NVIDIA NIM or Google Gemini)."""

from __future__ import annotations

import os
import time
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

# load_dotenv does not raise if .env is missing (e.g. on Render)
load_dotenv(override=True)

_client: OpenAI | None = None
_cached_provider: str | None = None


def _get_provider() -> str:
    provider = os.environ.get("LLM_PROVIDER", "").strip().lower()
    if provider == "nvidia":
        return "nvidia"
    return "gemini"


def _get_client_and_model() -> tuple[OpenAI, str]:
    global _client, _cached_provider
    provider = _get_provider()

    if _client is None or _cached_provider != provider:
        if provider == "nvidia":
            base_url = os.environ.get(
                "NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1"
            )
            api_key = os.environ.get("NVIDIA_API_KEY", "")
        else:
            base_url = os.environ.get(
                "GEMINI_BASE_URL",
                "https://generativelanguage.googleapis.com/v1beta/openai/",
            )
            api_key = os.environ.get("GEMINI_API_KEY", "")

        _client = OpenAI(base_url=base_url, api_key=api_key)
        _cached_provider = provider

    if provider == "nvidia":
        default_model = "nvidia/nemotron-3-super-120b-a12b"
        model = (
            os.environ.get("NVIDIA_MODEL")
            or os.environ.get("MODEL")
            or default_model
        )
    else:
        default_model = "gemini-3.8-flash"
        model = (
            os.environ.get("GEMINI_MODEL")
            or os.environ.get("MODEL")
            or default_model
        )

    return _client, model


def chat(
    system: str,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]] | None = None,
) -> Any:
    """Send a chat completion request and return the response object.

    *tools* uses OpenAI function-calling format::

        [{"type": "function", "function": {"name": ..., "parameters": ...}}]
    """
    client, model = _get_client_and_model()

    kwargs: dict[str, Any] = {
        "model": model,
        "max_tokens": 1024,
        "temperature": 0.2,
        "messages": [{"role": "system", "content": system}] + messages,
    }

    if tools:
        kwargs["tools"] = tools
        kwargs["tool_choice"] = "auto"

    for attempt in range(3):
        try:
            return client.chat.completions.create(**kwargs)
        except Exception as e:
            if "503" in str(e) and attempt < 2:
                time.sleep(2)
                continue
            raise
