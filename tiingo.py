import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os
# Your Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")
print(f"This is my API TOKEN: {API_TOKEN}"

# Parameters
symbol = "APPL"
start_date = "2024-01-01"
end_date = "2025-01-01"

url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
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
