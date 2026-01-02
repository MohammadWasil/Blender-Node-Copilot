import os
from typing import Optional

from .openai_client import call_openai
from data_utils.load_json import load_json

class OpenAICaller:
    """Simple wrapper for calling OpenAI via `call_openai`.

    Usage:
        caller = OpenAICaller()  # reads OPENAIKEY from env
        result = caller.send(system_prompt, "Make my cube red.")
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or self.get_api_key()

    @staticmethod
    def get_api_key() -> str:
        api_key = os.environ.get("OPENAIKEY")
        if not api_key:
            raise RuntimeError("OPENAIKEY environment variable not set")
        return api_key

    def send(self, system_prompt: dict, user_message: str = "Make my cube red."):
        result = call_openai(
            self.api_key,
            messages=[
                system_prompt,
                {"role": "user", "content": user_message},
            ],
        )
        return result

# need to call this when press "Enter" int the chatbox.
if __name__ == "__main__":
    caller = OpenAICaller()
    system_prompt = load_json("node_copilot/prompt/system_prompt.json")
    result = caller.send(system_prompt, user_message="Make my cube red.")
    print(result)