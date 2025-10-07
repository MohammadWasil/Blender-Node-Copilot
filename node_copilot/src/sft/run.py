from utils import load_config

from train import SupervisedFineTunedTrainer

def main():
    config_path = "/content/Blender-Node-Copilot/node_copilot/src/sft/config.yaml"
    config = load_config(config_path)

    input_prompt = "Can you make the sky look black?"

    sft_trainer = SupervisedFineTunedTrainer(config)
    if config["Process"]["SFT"]["Train"]:
        sft_trainer.train()
    else:
        answer = sft_trainer.inference(input_prompt)

if __name__ == "__main__":
    main()