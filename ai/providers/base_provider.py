# A base class for API providers, defining the interface and common properties for subclasses.

from typing import List, Optional


class BaseAPIProvider(object):
    def set_model(self, model_name: str):
        raise NotImplementedError("Subclass must implement set_model")

    def get_models(self) -> dict:
        raise NotImplementedError("Subclass must implement get_models")

    def generate_response(
        self, prompt: str, system_content: str, messages: Optional[List[dict]] = None
    ) -> str:
        raise NotImplementedError("Subclass must implement generate_response")
