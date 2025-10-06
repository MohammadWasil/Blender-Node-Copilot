from datasets import load_dataset

def load_dataset(dataset_path, dataset_file):
    training_data = load_dataset(path=dataset_path, data_files=dataset_file, split="train")
    return training_data

def set_device():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return device

