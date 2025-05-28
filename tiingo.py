import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

#Tiingo API token
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    print("⚠️Error API token is not found.")
    exit(1)

#Input + Parameters
stock_ticker = input(" Enter the stock ticker (e.g., AAPL, MSFT): ").strip().upper() #strip upper makes everything look neater. eg. m s f t to MSFT in the program
today_date_input = input(" Enter today's date (YYYY-MM-DD): ").strip()
try:
    end_date = datetime.strptime(today_date_input, "%Y-%m-%d").date()
except ValueError:
    print("❌ Invalid date format. Please use YYYY-MM-DD.")
    exit(1)
#It tries to run a piece of code inside the try block, and if an error happens, it jumps to the except block


try:
    short_holder = int(input(" Enter days for short-term moving average (e.g., 5): "))
    big_holder = int(input(" Enter days for long-term moving average (e.g., 200): "))
except ValueError:
    print("❌ Please enter integers for moving average periods.")
    exit(1)

#Date Stuff

start_date = end_date - timedelta(days=big_holder + 60)  # extra days because of weekends and public holidays
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")
print(f"\n Fetching data from {start_date_str} to {end_date_str}...\n") 
#ChatGPT gave me this code. I don't know 100% of how it works. But, it just makes the code neater: etc, Fetching data from xxxx-xx-xx to xxxx-xx-xx...





# Convert the dates to string format for the API 
# Not sure on how this works for now
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

print(f"Fetching data from {start_date} to {end_date_str}")


#URL and parameters for API request
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
if response.status_code != 200: #Not equal to 
    print("❌ Error fetching data. Status code:", response.status_code)
    exit(1)

#ABOVE IS FULLY DONE

#Before, the code above crashed whenever something bad happened
#Now, code prints out a warning sign even though the user made a mistake
#ChatGPT helped me with visuals, line 36, and taught me about try and excerpt






#Bellow is the default code given by MR MARKS
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
