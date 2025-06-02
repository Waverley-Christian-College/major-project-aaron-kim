import requests
import numpy as np  # For moving averages
from datetime import datetime, timedelta
import os

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
    short_holder = int(input("Enter days for short-term moving average (e.g., 5): "))
    big_holder = int(input("Enter days for long-term moving average (e.g., 200): "))
except ValueError:
    print("❌ Please enter integers for moving average periods.")
    exit(1)

# Date Stuff
start_date = end_date - timedelta(days=big_holder + 100)  # extra days for weekends/holidays
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")
print(f"\nFetching data from {start_date_str} to {end_date_str}...\n")

# --- Fetch stock price data ---
url = f"https://api.tiingo.com/tiingo/daily/{stock_ticker}/prices"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date_str,
    "endDate": end_date_str,
    "resampleFreq": "daily"
}

response = requests.get(url, headers=headers, params=params)
if response.status_code != 200:
    print(f"❌ Error fetching stock price data. Status code: {response.status_code}")
    print("Response:", response.text)  # Print the full response for more details
    exit(1)

# Process stock price data. i don't get this part.
data = response.json()
if not data:
    print("❌ No stock price data found.")
    exit(1)

dates = [entry["date"][:10] for entry in data]  # YYYY-MM-DD format
closes = [entry["close"] for entry in data]


#EZ
# Calculate Moving Averages using numpy convolution
if len(closes) < big_holder:
    print(f"❌ Not enough data to calculate {big_holder}-day moving average.")
    exit(1)

short_ma = np.convolve(closes, np.ones(short_holder)/short_holder, mode='valid')
long_ma = np.convolve(closes, np.ones(big_holder)/big_holder, mode='valid')

# Display results
#SEAN's PART
#HARD
print(f"\n{stock_ticker} Stock Data:")
print(f"Short-term ({short_holder}-day) Moving Average: {short_ma[-1]:.2f}")
print(f"Long-term ({big_holder}-day) Moving Average: {long_ma[-1]:.2f}")

# Buy/Hold/Sell Logic
if short_ma[-1] > long_ma[-1]:
    recommendation = "BUY"
    reason = "Golden Cross: The short-term moving average has crossed **above** the long-term moving average."
elif short_ma[-1] < long_ma[-1]:
    recommendation = "SELL"
    reason = "Death Cross: The short-term moving average has crossed **below** the long-term moving average."
else:
    recommendation = "HOLD"
    reason = "Neutral: The short-term and long-term moving averages are equal."

print(f"\nRecommendation: {recommendation}")
print(f"Reason: {reason}")
print("END RESULT")


#SEAN DEBUGGED EVERYTHING + MADE EVERYTHING LOOK BETTER + README + STARTING TEXT MESSAGE