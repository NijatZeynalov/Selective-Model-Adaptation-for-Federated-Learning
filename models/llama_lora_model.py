
import torch
import torch.nn as nn

class LlamaLoRaModel(nn.Module):
    def __init__(self):
        super(LlamaLoRaModel, self).__init__()
        self.fc1 = nn.Linear(512, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        """Forward pass for the Llama LoRa model."""
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
