from typing import List, Optional

from state_store.get_user_state import get_user_state

from ..ai_constants import DEFAULT_SYSTEM_CONTENT
from .anthropic import AnthropicAPI
from .openai import OpenAI_API
from .vertexai import VertexAPI

"""
New AI providers must be added below.
`get_available_providers()`
This function retrieves available API models from different AI providers.
It combines the available models into a single dictionary.
`_get_provider()`
This function returns an instance of the appropriate API provider based on the given provider name.
`get_provider_response`()
This function retrieves the user's selected API provider and model,
sets the model, and generates a response.
Note that context is an optional parameter because some functionalities,
such as commands, do not allow access to conversation history if the bot
isn't in the channel where the command is run.
"""


def get_available_providers():
    return {
        **AnthropicAPI().get_models(),
        **OpenAI_API().get_models(),
        **VertexAPI().get_models(),
    }


def _get_provider(provider_name: str):
    if provider_name.lower() == "anthropic":
        return AnthropicAPI()
    elif provider_name.lower() == "openai" or provider_name.lower() == "venice":
        return OpenAI_API()
    elif provider_name.lower() == "vertexai":
        return VertexAPI()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")


def get_provider_response(
    user_id: str,
    prompt: str,
    context: Optional[List] = [],
    system_content=DEFAULT_SYSTEM_CONTENT,
):
    try:
        try:
            provider_name, model_name = get_user_state(user_id, False)
        except FileNotFoundError:
            # Use default Venice model if user hasn't selected one
            provider_name = "venice"
            model_name = "zai-org-glm-4.6"
        
        provider = _get_provider(provider_name)
        provider.set_model(model_name)
        response = provider.generate_response(prompt, system_content, messages=context)
        return response
    except Exception as e:
        raise e
