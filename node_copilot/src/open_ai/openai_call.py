

import os

from openai_client import call_openai

def get_api_key() -> str:
    """
    Retrieves the OpenAI API key from environment variables.
    Raises an error if the key is not found.
    """
    api_key = os.environ.get("OPENAIKEY")
    if not api_key:
        raise RuntimeError("OPENAIKEY environment variable not set")
    return api_key

def main(api_key: str):
    result = call_openai(
        api_key,
        messages=[
            {"role": "system", "content": "You are a Blender assistant for generating Node Grpahs with the help of Python Code."},
            {"role": "user", "content": "Make my cube red."}
        ],
    )

    return result

if __name__ == "__main__":
    api_key = get_api_key()
    result = main(api_key)