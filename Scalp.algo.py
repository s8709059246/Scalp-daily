import yfinance as yf
import pandas as pd
import time

# 🔹 Config
TICKER = "NIFTY"   # aap stock ya index ka naam daal sakte ho
INTERVAL = "1m"    # candle time (1m for scalping)
LOOKBACK = 20      # moving average length

def fetch_data():
    data = yf.download(TICKER, period="1d", interval=INTERVAL)
    data['SMA'] = data['Close'].rolling(LOOKBACK).mean()
    return data

def check_signal(data):
    if data['Close'][-1] > data['SMA'][-1]:
        return "BUY 🔼"
    elif data['Close'][-1] < data['SMA'][-1]:
        return "SELL 🔽"
    else:
        return "HOLD ⏸️"

if __name__ == "__main__":
    while True:
        df = fetch_data()
        signal = check_signal(df)
        print(f"Last Price: {df['Close'][-1]:.2f} | Signal: {signal}")
        time.sleep(60)  # 1 minute delay
