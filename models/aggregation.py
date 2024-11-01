"""Aggregation strategies for federated learning."""
import torch

def federated_avg(client_params):
    global_params = {}
    for key in client_params[0].keys():
        global_params[key] = torch.mean(torch.stack([param[key] for param in client_params]), dim=0)
    return global_params