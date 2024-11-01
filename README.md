# Selective Model Adaptation for Federated Learning

This project implements a selective adaptation framework for federated learning using the LLaMA-2 7B model. The framework separates global and client-specific knowledge using Low-Rank Adaptation (LoRA) and shares only the global knowledge components with the server, while keeping client-specific updates local.

## Features
- Selective Parameter Sharing: Only the global knowledge components (LoRA A matrices) are shared with the server, while client-specific components (LoRA B matrices) are updated locally.
- LLaMA-2 7B with LoRA: Uses the LLaMA-2 7B model as the base model and applies LoRA for selective adaptation.
- Dynamic Aggregation: Server-side aggregation strategy updates the global model using shared A matrices from all clients.
- Privacy-Preserving: Minimizes the information shared with the server, improving privacy and reducing communication overhead.
- Performance Evaluation: Includes benchmarking tools for evaluating model performance in federated learning tasks across NLU and NLG tasks.

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/your_repo/selective-adaptation-fl.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your client datasets and place them in the `data/client_data/` directory.

## Usage
1. Configure the settings in `utils/config.py`, including the base model name, LoRA rank, and training hyperparameters.

2. Run the federated learning process:
   ```
   python main.py
   ```

3. Evaluate the trained model:
   ```
   python evaluate.py
   ```

## License
This project is licensed under the MIT License. See `LICENSE` for more information.