import requests
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any

from langchain_community.llms.utils import enforce_stop_tokens


class CustomLLM(LLM):
    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted")
        return prompt[:self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}


class MyQwen(LLM):
    history = []

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "Qwen"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        data = {'text': prompt}
        url = "http://127.0.0.1:7211/chat/"
        response = requests.post(url, json=data)
        if response.status_code != 200:
            return "error"
        resp = response.json()
        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        self.history = self.history + [[None, resp['result']]]
        return resp['result']
