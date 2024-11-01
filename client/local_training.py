
import torch

def train_model(model, data_loader, optimizer, criterion, num_epochs=10):
    """Train the model locally."""
    for epoch in range(num_epochs):
        model.train()
        for batch_idx, (data, target) in enumerate(data_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

        # Save checkpoint
        torch.save(model.state_dict(), f'checkpoint_epoch_{epoch}.pth')
        print(f'Epoch {epoch} completed with loss: {loss.item()}')
