#Is It a Good Time to Buy This Tool? 💀💀

This Python script helps determine whether it's a good time to **buy**, **sell**, or **hold** a stock by calculating:
-  The **short-term (e.g., 50-day)** moving average
-  The **long-term (e.g., 200-day)** moving average
-  (Coming soon) Graham Number and valuation metrics

It pulls historical stock data from the **Tiingo API**, performs the analysis, and gives a final recommendation.

Special features 😈😈😈

-Calculating short and long term averages
-Fetching data securely using the tiingo api token
-Advising whether or not to buy a particular stock 
-Detects the Golden/Death cross patterns
-Error handling 
-Automatic date range calculation

### How to Run the Script (Without GitHub)

1. **Install Python**
   Download and install Python from the official website:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Install Required Packages**
   Open your terminal or command prompt and run:

   ```bash
   pip install requests numpy
   ```

3. **Set Your Tiingo API Token**

   * Get your Tiingo API token from [https://api.tiingo.com/](https://api.tiingo.com/)
   * Set it as an environment variable named `API_TOKEN` on your system
     (or update the script to insert your token directly for testing)

4. **Download the Python script** (e.g., `stock_analysis.py`) and save it locally.

5. **Run the script** from your terminal/command prompt:

   ```bash
   python stock_analysis.py
   ```

6. **Follow the prompts** to enter:

   * The stock ticker symbol (e.g., AAPL)
   * The date you want to analyze (YYYY-MM-DD)
   * The number of days for short-term and long-term moving averages

The script will then fetch data, calculate moving averages, and give you a buy/hold/sell recommendation.

---
