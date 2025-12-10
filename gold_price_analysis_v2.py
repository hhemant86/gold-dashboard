import pandas as pd
import matplotlib.pyplot as plt

# Version 2: Gold Price Analysis with SMA & EMA Indicators

# 1. Load Data
file_path = "historical_gold.csv"  # Same CSV file as Version 1

try:
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
except Exception as e:
    print("Error loading file:", e)
    df = None

if df is not None:
    print("\nLast 5 rows:")
    print(df.tail(5))

    # 2. Calculate SMA
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['SMA_10'] = df['Close'].rolling(window=10).mean()

    # 3. Calculate EMA
    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()

    # 4. Plot Price + SMAs + EMAs
    plt.figure(figsize=(14, 6))

    plt.plot(df['Date'], df['Close'], label="Close Price")
    plt.plot(df['Date'], df['SMA_5'], label="SMA 5")
    plt.plot(df['Date'], df['SMA_10'], label="SMA 10")
    plt.plot(df['Date'], df['EMA_5'], label="EMA 5")
    plt.plot(df['Date'], df['EMA_10'], label="EMA 10")

    plt.title("Gold Price with SMA & EMA Indicators")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Cannot plot because data failed to load.")
