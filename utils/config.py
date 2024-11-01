
import os

# Example configuration
LEARNING_RATE = float(os.getenv("LEARNING_RATE", 0.01))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 32))
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS", "localhost:5000")
