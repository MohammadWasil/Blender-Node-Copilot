import json
import urllib.request
import urllib.error
import ssl

OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def call_openai(
    api_key: str,
    messages: list,
    model: str = "gpt-4.1-mini",
    temperature: float = 0.3,
    timeout: int = 30,
):
    """
    Calls OpenAI Chat Completions API.

    messages example:
    [
        {"role": "system", "content": "You are a Blender assistant for generating Node Grpahs with the help of Python Code."},
        {"role": "user", "content": "Make my cube red."}
    ]
    """

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    data = json.dumps(payload).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    request = urllib.request.Request(
        OPENAI_API_URL,
        data=data,
        headers=headers,
        method="POST",
    )

    # Create SSL context (important for Blender on some systems)
    context = ssl.create_default_context()

    try:
        with urllib.request.urlopen(request, context=context, timeout=timeout) as response:
            response_data = response.read().decode("utf-8")
            result = json.loads(response_data)

            return result["choices"][0]["message"]["content"]

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise RuntimeError(f"OpenAI HTTP error {e.code}: {error_body}")

    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}")

    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")
