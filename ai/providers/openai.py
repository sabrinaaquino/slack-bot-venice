import openai
from .base_provider import BaseAPIProvider
import os
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class OpenAI_API(BaseAPIProvider):
    MODELS = {
        "zai-org-glm-4.6": {
            "name": "GLM 4.6",
            "provider": "Venice",
            "max_tokens": 8192,
        },
        "venice-uncensored": {
            "name": "Venice Uncensored",
            "provider": "Venice",
            "max_tokens": 8192,
        },
        "qwen3-235b-a22b-instruct-2507": {
            "name": "Qwen3 235B Instruct",
            "provider": "Venice",
            "max_tokens": 8192,
        },
    }

    def __init__(self):
        self.api_key = os.environ.get("VENICE_API_KEY")
        self.current_model = "zai-org-glm-4.6"

    def set_model(self, model_name: str):
        if model_name not in self.MODELS.keys():
            raise ValueError("Invalid model")
        self.current_model = model_name

    def get_models(self) -> dict:
        if self.api_key is not None:
            return self.MODELS
        else:
            return {}

    def generate_response(self, prompt: str, system_content: str, messages=None) -> str:
        try:
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url="https://api.venice.ai/api/v1"
            )
            
            # Build messages array
            chat_messages = [{"role": "system", "content": system_content}]
            
            # Add conversation history if provided
            if messages:
                for msg in messages:
                    # Skip messages with empty or None text
                    text = msg.get("text")
                    if not text or not text.strip():
                        continue
                    role = "assistant" if msg.get("bot_id") else "user"
                    chat_messages.append({"role": role, "content": text})
            
            # Add current prompt
            chat_messages.append({"role": "user", "content": prompt})
            
            response = self.client.chat.completions.create(
                model=self.current_model,
                messages=chat_messages,
                max_tokens=self.MODELS[self.current_model]["max_tokens"],
            )
            return response.choices[0].message.content
        except openai.APIConnectionError as e:
            logger.error(f"Server could not be reached: {e.__cause__}")
            raise e
        except openai.RateLimitError as e:
            logger.error(f"A 429 status code was received. {e}")
            raise e
        except openai.AuthenticationError as e:
            logger.error(f"There's an issue with your API key. {e}")
            raise e
        except openai.APIStatusError as e:
            logger.error(
                f"Another non-200-range status code was received: {e.status_code}"
            )
            raise e
