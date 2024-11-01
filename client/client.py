"""Client-side code for selective adaptation."""
import torch
from models.llama_lora_model import LLaMALoRAModel
from client.local_training import train_local_model


class Client:
    def __init__(self, client_id, base_model_name, lora_rank, client_data):
        self.client_id = client_id
        self.model = LLaMALoRAModel(base_model_name, lora_rank)
        self.data = client_data

    def train(self, num_epochs, batch_size, learning_rate):
        train_local_model(self.model, self.data, num_epochs, batch_size, learning_rate)

    def get_global_params(self):
        global_params = {}
        for lora_layer in self.model.lora_layers:
            global_params[lora_layer.name] = lora_layer.A
        return global_params

    def update_global_params(self, global_params):
        for lora_layer in self.model.lora_layers:
            lora_layer.A.data = global_params[lora_layer.name]