
#Completed
import requests
import json
   from datetime import date, timedelta
import matplotlib.pyplot as plt
import os

# Your Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")
print(f"This is my API TOKEN: {API_TOKEN}")

# Parameters
stock_ticker = input("Please enter the stock ticker (e.g., AAPL, MSFT): ")
today_date = input("what is the date Today? ")





#ERRORS


starting_date = today_date - timedelta(days=200) # today's date and 200 days backwards

# Convert the dates to string format for the API 
# Not sure on how this works for now
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

print(f"Fetching data from {Starting_date} to {today_date_str}")









#rest is not edited


url = f"https://api.tiingo.com/tiingo/daily/{stock_ticker}/prices"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}
params = {
    "startDate": start_date,
    "endDate": end_date,
    "resampleFreq": "daily"
}

# Make the request
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract dates and closing prices
dates = [entry["date"][:10] for entry in data]
closes = [entry["close"] for entry in data]

# Plotting
plt.figure(figsize=(20, 5))
plt.plot(dates, closes, marker='o')
plt.title(f"{symbol} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig("stock_chart_tiingo.png")
