import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA
file_path = "historical_gold.csv"  # CSV must be in same folder

try:
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
except Exception as e:
    print("Error loading file:", e)
    df = None

# 2. PRINT LAST 5 ROWS
if df is not None:
    print(df.tail(5))  # Print before showing chart

    # 3. PLOT PRICE
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Close'])
    plt.title('Gold Price (XAUUSD) Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Cannot plot because data failed to load.")
