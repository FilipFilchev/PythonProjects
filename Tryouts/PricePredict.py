# Rate of change (ROC) = Close(t) / Close(t-n) * 100
# import websocket for live data
# make Excel Tables with json & pandas dics

import pandas as pd
import websocket 
from binance.clinet import Client
client = Client(api_key, api_secret)

stream = websocket.connect('wss://stream.binance.com...')

async with stream as receiver:
    data = await receiver.recv()
    data = json.loads(data)['data']
    df = createframe(data)
    print(df)
    
def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.l0c[:,['s','E','c']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(pd.Time, unit='ms')
    return df


""" 
1. Setup Development Environment


requests: for making API calls.
numpy, pandas: for data manipulation.
ta: for technical indicators.

```
pip install requests numpy pandas ta
```

1. Get Binance API Keys
Register for a Binance account and generate API keys. Store the API key and secret securely.

2. Code the Bot:
2.1. Connect to Binance API
To ensure that we can connect to Binance, let's create a simple function to test the connection:

```
import requests

BASE_URL = "https://api.binance.com"

def test_connection():
    response = requests.get(f"{BASE_URL}/api/v3/ping")
    return response.status_code == 200
```

2.2. Fetch Market Data
To make trading decisions, you'll need market data. Here's a function to get recent candlestick data:

```
def get_klines(symbol, interval, limit=50):
    endpoint = f"{BASE_URL}/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(endpoint, params=params)
    return response.json()

```

2.3. Define Trading Strategy
For this example, let's use a simple moving average crossover strategy:

Buy when the short-term moving average crosses above the long-term moving average.
Sell when the short-term moving average crosses below the long-term moving average.


```
import pandas as pd
import ta

def generate_signals(symbol, interval):
    data = get_klines(symbol, interval)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['close'] = df['close'].astype(float)
    
    # Calculate moving averages
    df['short_ma'] = ta.trend.sma_indicator(df['close'], window=10)
    df['long_ma'] = ta.trend.sma_indicator(df['close'], window=50)
    
    # Generate signals
    df['signal'] = 0.0
    df.loc[df['short_ma'] > df['long_ma'], 'signal'] = 1.0
    df.loc[df['short_ma'] <= df['long_ma'], 'signal'] = -1.0

    return df['signal'].iloc[-1]

```


2.4. Execute Orders
You'll need functions to place buy and sell orders:

```
API_KEY = 'YOUR_BINANCE_API_KEY'
API_SECRET = 'YOUR_BINANCE_API_SECRET'

def place_order(symbol, side, quantity, order_type='MARKET'):
    endpoint = f"{BASE_URL}/api/v3/order"
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    data = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': quantity,
        'timestamp': int(time.time() * 1000)
    }
    
    signature = hmac.new(bytes(API_SECRET , 'latin-1'), msg=urllib.parse.urlencode(data).encode('utf-8') , digestmod = hashlib.sha256).hexdigest()
    data['signature'] = signature
    
    response = requests.post(endpoint, headers=headers, data=data)
    return response.json()

```

2.5. Risk Management
Always set a stop loss and take profit when trading, especially with leverage:

```
def place_order_with_risk_management(symbol, side, quantity, stop_loss, take_profit):
    # Place main order
    response = place_order(symbol, side, quantity)
    
    if response['status'] == 'FILLED':
        # Place OCO (One Cancels the Other) order for stop loss and take profit
        place_oco_order(symbol, side, quantity, stop_loss, take_profit)
    
    return response
```


2.6. Main Loop
This loop will check for signals and execute trades:

```
def main():
    while True:
        signal = generate_signals('BTCUSDT', '5m')
        
        if signal == 1.0:
            # Buy logic
            pass
        elif signal == -1.0:
            # Sell logic
            pass
        
        time.sleep(300) # Sleep for 5 minutes
```

3. Considerations:
Leverage and Margin: If you're considering using leverage, understand that it increases both potential profits and potential losses. Make sure to adjust your risk management strategy accordingly.
Rate Limits: Always check and respect the API rate limits.
NO RISK NO PROFIT ;)

Backtesting: Before deploying any trading strategy, it's crucial to backtest it on historical data to see how it would have performed.
Paper Trading: Before trading with real money, test your bot in a paper trading environment to ensure it behaves as expected.


## Some techniques:

Time Series Analysis:
Quantative Analyses (Mathematical Alpha search) & Sentimental Analyses (Data, News, WebScrapping)

ARIMA (Autoregressive Integrated Moving Average): Used for forecasting financial time series data.
GARCH (Generalized Autoregressive Conditional Heteroskedasticity): Used to model volatility in financial markets.
LSTM (Long Short-Term Memory): A type of recurrent neural network (RNN) particularly well-suited for sequence prediction problems, like time series forecasting.
Prophet: Developed by Facebook, it's a forecasting tool designed for business applications.
Supervised Learning:

Random Forests and Gradient Boosting Machines (like XGBoost): Used for prediction tasks based on historical data.
Support Vector Machines (SVM): Often used for classification tasks in trading, like predicting market upturns or downturns.
Neural Networks: Multi-layer perceptrons (MLP) or deep learning architectures can be used for prediction tasks.
Unsupervised Learning:

PCA (Principal Component Analysis): Used for dimensionality reduction in financial datasets.
Clustering (e.g., K-means, DBSCAN): Used to identify patterns or groups in the data, like clustering stocks with similar behaviors.
Reinforcement Learning:

Algorithms like Q-learning, Deep Q Networks (DQN), and Proximal Policy Optimization (PPO) have been explored for algorithmic trading. These models learn by interacting with an environment (like a simulated market) to maximize some notion of cumulative reward.

Sentiment Analysis:
Analyzing news articles, financial reports, or social media to gauge market sentiment. Techniques like natural language processing (NLP) and sentiment scoring are employed.

Anomaly Detection:
Used to identify outliers or unusual patterns in financial data, which could indicate fraudulent activity or market manipulation. Techniques like the Isolation Forest or One-Class SVM are commonly used.

Portfolio Optimization:
Techniques like the Markowitz Efficient Frontier can be combined with machine learning models to construct optimal portfolios.

Feature Engineering:
Creating new variables from raw data can be as crucial as the algorithm itself. Technical indicators like Moving Average Convergence Divergence (MACD), Relative Strength Index (RSI), and Bollinger Bands are examples in the context of trading.

Ensemble Learning:
Combining predictions from multiple models to achieve a more accurate and robust prediction.

Algorithmic Execution:
ML can be used not just for deciding when to trade but also how to execute those trades most efficiently, especially in high-frequency trading scenarios.

"""