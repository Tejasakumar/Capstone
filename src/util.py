import os
import numpy as np
import torch
from torch.utils.data import Dataset

def write_pred(test_pred, test_idx, file_path):
    """Writes predictions to a CSV file."""
    test_pred = [item for sublist in test_pred for item in sublist]
    with open(file_path, 'w') as f:
        for idx, pred in zip(test_idx, test_pred):
            print(f"{idx.upper()},{pred[0]}", file=f)

class ExeDataset(Dataset):
    """Custom dataset class for loading executable files."""
    
    def __init__(self, data_path_benign, data_path_malicious, first_n_byte=2000000):
        self.fp_list = []
        self.label_list = []
        self.first_n_byte = first_n_byte
        
        # Load benign files
        for filename in os.listdir(data_path_benign):
                self.fp_list.append(os.path.join(data_path_benign, filename))
                self.label_list.append(0)  # Label for benign files

        # Load malicious files
        for filename in os.listdir(data_path_malicious):
                self.fp_list.append(os.path.join(data_path_malicious, filename))
                self.label_list.append(1)  # Label for malicious files

    def __len__(self):
        return len(self.fp_list)

    def __getitem__(self, idx):
        """Loads a single executable file and its label."""
        file_path = self.fp_list[idx]
        
        try:
            with open(file_path, 'rb') as f:
                tmp = [i + 1 for i in f.read()[:self.first_n_byte]]
                tmp += [0] * (self.first_n_byte - len(tmp))  # Pad with zeros
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            tmp = [0] * self.first_n_byte  # Return a zero-filled array if there's an error

        return np.array(tmp), np.array([self.label_list[idx]])