from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import SFTConfig, SFTTrainer

from process_data import format_dataset
from config import SFTConfiguration

from data_loader import set_device, load_data

from inference import inference

import mlflow

class SupervisedFineTunedTrainer:
    def __init__(self, config):
        self.config = config
        
        self.device = set_device()
        self.model = self.config["Model"]["model_name"]
        
        self.dataset_path = self.config["Data"]["dataset_path"]
        self.dataset_file = self.config["Data"]["dataset_file"]

        if self.config["Process"]["SFT"]["Train"]:
            self.training_data = load_data(self.dataset_path, self.dataset_file)
            self.dataset = self.get_dataset()

        self.tokenizer = self.load_tokenizer()
        self.model = self.load_model()
        self.sftconfiguration = SFTConfiguration(self.config)
        self.sft_config = self.sftconfiguration.get_sft_config()

        mlflow.set_experiment("Supervised Fine Tuning QWEN2.5 Coder 0.5B v0.1")
        
    def load_tokenizer(self):
        tokenizer =  AutoTokenizer.from_pretrained(pretrained_model_name_or_path=self.model)
                
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.unk_token_id
        #tokenizer.chat_template
        return tokenizer

    def load_model(self,):
        if self.config["Process"]["SFT"]["Train"]:
            return AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model).to(self.device)
        else:
            # load the model from the output directory
            #return AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=self.model, device_map="auto", torch_dtype="auto")
            pass

    def get_dataset(self):
        dataset = self.training_data.map(format_dataset)
        dataset = dataset.remove_columns(['prompt', 'completion'])
        messages = dataset[0]['messages']
        return dataset

    def train(self):
        
        print("Training started...")
        
        trainer = SFTTrainer(
            model=self.model,
            processing_class=self.tokenizer,
            args=self.sft_config,
            train_dataset=self.dataset,
        )

        #dl = trainer.get_train_dataloader()
        #batch = next(iter(dl))

        with mlflow.start_run() as run:
          mlflow.transformers.autolog(log_models=False)
          mlflow.log_param("epochs", self.config["Train"]["num_train_epochs"])

          trainer.train()
        print(f"MLflow Run ID: {run.info.run_id}")

    
    def inference(self, sentence):
        print("Input Prompt: ", sentence)
        answer = inference(sentence, self.model, self.tokenizer)

        print("Output: ", answer)
        return answer