"""Utility functions for data loading and preprocessing."""
import os
import torch
from datasets import load_dataset


def load_client_data(data_dir):
    client_data = {}
    for client_dir in os.listdir(data_dir):
        client_id = int(client_dir.split("client")[1])
        dataset = load_dataset(os.path.join(data_dir, client_dir))
        client_data[client_id] = dataset
    return client_data


def preprocess_data(dataset, tokenizer, max_length):
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=max_length)

    dataset = dataset.map(tokenize_function, batched=True)
    dataset = dataset.map(lambda examples: {"labels": examples["input_ids"]}, batched=True)
    dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
    return dataset