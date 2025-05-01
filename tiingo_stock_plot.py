# File: tiingo_stock_plot.py

import requests
import json
import matplotlib.pyplot as plt
import os
# --- Tiingo API Configuration ---
API_TOKEN = "os.genenv()"  # Replace with your actual token
symbol = "NVDA"
start_date = "2025-01-01"
end_date = "2025-04-01"

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

try:
    print(f"🔄 Fetching stock data for {symbol} from Tiingo...")
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=4))

    '''dates = [entry["date"][:10] for entry in data]
    closes = [entry["close"] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, closes, marker='o')
    plt.title(f"{symbol} Closing Prices from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()'''

except requests.exceptions.RequestException as e:
    print(f"❌ API request failed: {e}")
except (KeyError, IndexError, TypeError) as e:
    print(f"❌ Data processing failed: {e}")
