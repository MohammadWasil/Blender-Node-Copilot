import trl
from trl import SFTConfig, SFTTrainer

model_name = "Qwen/Qwen2.5-Coder-0.5B"

class SFTConfiguration:
    def __init__(self, config):
        self.config = config

    def get_sft_config(self):

        sft_config = SFTConfig(
            ## GROUP 1: Memory usage
            # These arguments will squeeze the most out of your GPU's RAM
            # Checkpointing
            gradient_checkpointing=True,    # this saves a LOT of memory
            # Set this to avoid exceptions in newer versions of PyTorch
            gradient_checkpointing_kwargs={'use_reentrant': False},
            # Gradient Accumulation / Batch size
            # Actual batch (for updating) is same (1x) as micro-batch size
            gradient_accumulation_steps=1,
            # The initial (micro) batch size to start off with
            per_device_train_batch_size=4,
            # If batch size would cause OOM, halves its size until it works
            auto_find_batch_size=True,

            ## GROUP 2: Dataset-related
            max_length=int(self.config["Train"]["max_length"]), # renamed in v0.20
            # Dataset
            # packing a dataset means no padding is needed
            packing=True,
            packing_strategy='wrapped', # added to approximate original packing behavior

            ## GROUP 3: These are typical training parameters
            num_train_epochs=int(self.config["Train"]["num_train_epochs"]),
            learning_rate=float(self.config["Train"]["learning_rate"]),
            # Optimizer
            # 8-bit Adam optimizer - doesn't help much if you're using LoRA!
            # optim='paged_adamw_8bit',

            ## GROUP 4: Logging parameters
            logging_steps=int(self.config["Logging"]["logging_steps"]),
            logging_dir=self.config["Logging"]["logging_dir"],
            output_dir=self.config["Logging"]["output_dir"],
            report_to=self.config["Logging"]["report_to"],

            # ensures bf16 (the new default) is only used when it is actually available
            # bf16=torch.cuda.is_bf16_supported(including_emulation=False)
        )

        return sft_config
