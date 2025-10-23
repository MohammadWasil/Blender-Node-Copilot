"""
Source : https://huggingface.co/learn/llm-course/en/chapter11/4
"""
from peft import LoraConfig

class LoraConfiguration:
  def __init__(self, config):

    self.config = config

    # TODO: Configure LoRA parameters
    # r: rank dimension for LoRA update matrices (smaller = more compression)
    self.rank_dimension = self.config["Train"]["LORA"]["rank_dimension"]
    # lora_alpha: scaling factor for LoRA layers (higher = stronger adaptation)
    self.lora_alpha = self.config["Train"]["LORA"]["lora_alpha"]
    # lora_dropout: dropout probability for LoRA layers (helps prevent overfitting)
    self.lora_dropout = self.config["Train"]["LORA"]["lora_dropout"]

  def get_lora_config(self):
    
    peft_config = LoraConfig(
        r=self.rank_dimension,  # Rank dimension - typically between 4-32
        lora_alpha=self.lora_alpha,  # LoRA scaling factor - typically 2x rank
        lora_dropout=self.lora_dropout,  # Dropout probability for LoRA layers
        bias="none",  # Bias type for LoRA. the corresponding biases will be updated during training.
        target_modules="all-linear",  # Which modules to apply LoRA to
        task_type="CAUSAL_LM",  # Task type for model architecture
    )

    return peft_config