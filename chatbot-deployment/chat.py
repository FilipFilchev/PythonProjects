#ORIGINAL
import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)



"""

A model.pth file is a file that contains the state of a PyTorch model. The state of a model includes the model's parameters (weights and biases) and optimizer state (such as the learning rate and the current step count).

Here's a simple example of how to save and load a PyTorch model to/from a .pth file:

python
Copy code
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

In this example, we first define a simple PyTorch model called SimpleModel which is a single linear layer (torch.nn.Linear).
 Then, we create an instance of the model called model and save its state to a .pth file using torch.save(model.state_dict(), 
 "model.pth"). Finally, we load the saved state of the model from the .pth file using torch.load("model.pth") and 
 create a new instance of the model called loaded_model and
  load its state using loaded_model.load_state_dict(torch.load("model.pth")).

"""



"""import random
import json

import torch
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()

class NeuralNet(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNet, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def tokenize(sentence):
    words = nltk.word_tokenize(sentence)
    words = [wordnet_lemmatizer.lemmatize(word.lower()) for word in words]
    return words

def bag_of_words(sentence, words):
    sentence_words = tokenize(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return bag

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "model.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
        """

"""
        To implement a working console chatbot into a React project with already rendered style and HTML, you can follow these steps:

Create a new component in React for the chatbot.
Set up a user input form within the component that will send a message to the chatbot when submitted.
Send the user's message to the backend, where the chatbot logic will be implemented.
The backend will receive the user's message, process it using the pre-trained model, and return a response to the frontend.
The frontend will then receive the chatbot's response and display it in the chat interface.
Repeat the process for each subsequent message between the user and the chatbot.
You can use any programming language and technology stack for the backend, such as Flask or Django for Python, Node.js for JavaScript, or Ruby on Rails for Ruby.
It is also possible to implement the chatbot logic directly in the frontend using JavaScript, although this is not recommended due to security and scalability concerns."""