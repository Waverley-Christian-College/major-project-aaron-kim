import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
import numpy as np  # Import numpy for moving averages

# Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    print("⚠️ Error: API token is not found.")
    exit(1)

# Input + Parameters
stock_ticker = input("Enter the stock ticker (e.g., AAPL, MSFT): ").strip().upper()  #strip upper makes everything look neater. eg. m s f t to MSFT in the program
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
start_date = end_date - timedelta(days=big_holder + 60)  # extra days because of weekends and public holidays
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")
print(f"\nFetching data from {start_date_str} to {end_date_str}...\n")

# URL and parameters for API request
url = f"https://api.tiingo.com/tiingo/daily/{stock_ticker}/prices"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date_str,  # Use the string version of the date
    "endDate": end_date_str,      # Use the string version of the date
    "resampleFreq": "daily"
}

# Make the request
response = requests.get(url, headers=headers, params=params)
if response.status_code != 200:
    print("❌ Error fetching data. Status code:", response.status_code)
    exit(1)

    # Extract dates and closing prices
    data = response.json()
    dates = [entry["date"][:10] for entry in data]  # Ensure we have the date format YYYY-MM-DD
    closes = [entry["close"] for entry in data]

    # Calculate Moving Averages
    short_ma = np.convolve(closes, np.ones(short_holder)/short_holder, mode='valid')
    long_ma = np.convolve(closes, np.ones(big_holder)/big_holder, mode='valid')
