#Trading predictions based on CSV-file data set
# Import necessary libraries
import pandas as pd
from transformers import BertForSequenceClassification, BertTokenizer

# Load the pre-trained BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Read in financial data using CSV file
df = pd.read_csv('stock_data.csv')

# Clean and organize data
df = df.dropna()
df = df[['date', 'text', 'close']]

# Split data into training and testing sets
train_data = df[:int(len(df)*0.8)]
test_data = df[int(len(df)*0.8):]

# Encode text data for BERT
def encode_text(text):
    encoded = tokenizer.encode(text, add_special_tokens=True)
    return encoded

# Prepare data for fine-tuning
X_train = train_data['text'].apply(encode_text)
y_train = train_data['close']

# Fine-tune the BERT model on the financial data
model.fit(X_train, y_train)

# Make predictions
def make_prediction(text):
    encoded = encode_text(text)
    prediction = model.predict(encoded)
    return prediction

# Display data and predictions
print("Last stock price: ", df['close'].tail(1))
print("Prediction for next day's closing price: ", make_prediction(df['text'].tail(1)))