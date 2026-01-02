import json
import yaml
from pathlib import Path

def load_config(config_path : str) -> str:
    """Load configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_json(filename):
    """Load data from a JSON file."""
    with open(filename, 'r') as f:
        training_data = json.load(f)
    return training_data

def load_text_file(file_path):
    """Load text from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def save_json(data : dict, output_path : Path) -> None:
    """Save data to a JSON file."""
    #output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    config = load_config(config_path="config.yaml")

    # Define the output path
    input_path = Path(config["Prompt"]["prompts_example"])
    print(input_path)
    
    # Save the example data
    initial_training_data = load_json(input_path)

    root_python_script = Path(config["Prompt"]["input_python_scripts"])
    
    training_data = []
    
    for material_script in initial_training_data:
        
        material_dict = {}

        script_path = root_python_script / Path(material_script["output"])
        py_scripts = load_text_file(script_path)
        material_dict["prompt"] = material_script["input"]
        material_dict["completion"] = py_scripts
        training_data.append(material_dict)
    
    save_json(training_data, Path(config["Prompt"]["training_data"]))
    
