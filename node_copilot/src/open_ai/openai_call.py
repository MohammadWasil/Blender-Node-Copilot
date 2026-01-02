import os

from .openai_client import call_openai
from data_utils.load_json import load_json

def get_api_key() -> str:
    """
    Retrieves the OpenAI API key from environment variables.
    Raises an error if the key is not found.
    """
    api_key = os.environ.get("OPENAIKEY")
    if not api_key:
        raise RuntimeError("OPENAIKEY environment variable not set")
    return api_key

def main(api_key: str, system_prompt: dict):
    result = call_openai(
        api_key,
        messages=[
            system_prompt,
            {"role": "user", "content": "Make my cube red."}
        ],
    )
    return result

if __name__ == "__main__":
    # get your key
    api_key = get_api_key()

    # Load System Prompt Example
    system_prompt = load_json("/mnt/d/Blender/Blender Node Copilot/node_copilot/prompt/system_prompt.json")

    result = main(api_key, system_prompt)
    print(result)