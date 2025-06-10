import requests
import numpy as np  # For moving averages
from datetime import datetime, timedelta
import os

print("Hi! I’m your stock analysis assistant.")
print("Just tell me the stock ticker you want and the date you’re interested in.")
print("I’ll grab the latest price data for you, calculate short-term and long-term moving averages.")
print("Then tell you whether it’s a good time to buy, hold, or sell based on how those averages compare.")
print("Easy, quick, and data-driven — I’ve got your back for smarter trading decisions!")

start = input("Would you like to begin? (yes/no): ").strip().lower()

if start == "yes":
    print("Lets begin!")
    # Tiingo API token
    API_TOKEN = os.getenv("API_TOKEN")
    if not API_TOKEN:
        print("⚠️ Error: API token is not found.")
        exit(1)

    # Input + Parameters
    stock_ticker = input("Enter the stock ticker (e.g., AAPL, MSFT): ").strip().upper()
    today_date_input = input("Enter today's date (YYYY-MM-DD): ").strip()

    try:
        end_date = datetime.strptime(today_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        exit(1)

    try:
        short_holder = int(input("Enter days for short-term moving average (e.g., 50): "))
        big_holder = int(input("Enter days for long-term moving average (e.g., 200): "))
    except ValueError:
        print("❌ Please enter integers for moving average periods.")
        exit(1)

    # --- Date setup ---
    start_date = end_date - timedelta(days=big_holder + 100)  # Buffer for holidays/weekends
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    print(f"\nFetching data from {start_date_str} to {end_date_str}...\n")

    # --- Fetch stock price data ---
    price_url = f"https://api.tiingo.com/tiingo/daily/{stock_ticker}/prices"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}"
    }
    params = {
        "startDate": start_date_str,
        "endDate": end_date_str,
        "resampleFreq": "daily"
    }

    response = requests.get(price_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"❌ Error fetching stock price data. Status code: {response.status_code}")
        print("Response:", response.text)
        exit(1)

    data = response.json()
    if not data:
        print("❌ No stock price data found.")
        exit(1)

    closes = [entry["close"] for entry in data]
    if len(closes) < big_holder:
        print(f"❌ Not enough data to calculate {big_holder}-day moving average.")
        exit(1)

    # --- Calculate Moving Averages ---
    short_ma = np.convolve(closes, np.ones(short_holder)/short_holder, mode='valid')
    long_ma = np.convolve(closes, np.ones(big_holder)/big_holder, mode='valid')

    # --- Display Results ---
    print(f"\n{stock_ticker} Stock Data:")
    print(f"Short-term ({short_holder}-day) Moving Average: {short_ma[-1]:.2f}")
    print(f"Long-term ({big_holder}-day) Moving Average: {long_ma[-1]:.2f}")

    print("\n📊 Trading Signal Analysis")
    if short_ma[-1] > long_ma[-1]:
        recommendation = "BULLISH + BUY"
        reason = "📈 Golden Cross detected – short-term moving average is above the long-term."
    elif short_ma[-1] < long_ma[-1]:
        recommendation = "BEARISH + SELL"
        reason = "📉 Death Cross detected – short-term moving average is below the long-term."
    else:
        recommendation = "HOLD"
        reason = "➖ Moving averages are equal – no clear signal."

    print(f"\nRecommendation: {recommendation}")
    print(f"Reason: {reason}")
    print("END RESULT")

else:
    print(":(")