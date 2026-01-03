from pathlib import Path

from src.open_ai.openai_call import OpenAICaller
from src.data_utils.load_json import load_json
from src.blender_ui.data import state

def worker(user_messages):
    caller = OpenAICaller()
    
    system_prompt_path = Path(__file__).resolve().parents[3] / "prompt" / "system_prompt.json"
    system_prompt = load_json(system_prompt_path)
    
    state.llm_result = caller.send(system_prompt, user_message=user_messages)