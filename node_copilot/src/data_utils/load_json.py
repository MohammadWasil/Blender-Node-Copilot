import json
import os
import importlib.resources as resources

def load_json(file_path: str):    
    with open(file_path, 'r') as f:
        return json.load(f)

def load_system_prompt():
    with resources.open_text("prompt", "system_prompt.json", encoding="utf-8") as f:
        return json.load(f)

    #base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #prompt_path = os.path.join(base_dir, "prompt", "system_prompt.json")
    #with open(prompt_path, "r", encoding="utf-8") as f:
    #    return json.load(f)