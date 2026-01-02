import json
import importlib.resources as resources

def load_json(file_path: str):    
    with open(file_path, 'r') as f:
        return json.load(f)

def load_system_prompt():
    with resources.open_text("node_copilot.prompt", "system_prompt.json", encoding="utf-8") as f:
        return json.load(f)