import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.fc2 = nn.Linear(hidden_size, hidden_size) 
        self.fc3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        # no activation and no softmax at the end
        return out


import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(in_features=10, out_features=1)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the model
model = SimpleModel()

# Save the model state to a .pth file
torch.save(model.state_dict(), "model.pth")

# Load the saved model state from the .pth file
loaded_model = SimpleModel()
loaded_model.load_state_dict(torch.load("model.pth"))
