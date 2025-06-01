[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9x6qoLrK)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19374584)
# 💸 Is it a good time to buy?

This Python script checks if it's a good time to buy a stock by calculating the 5-day moving average (MA), the 200-day moving average (MA), and the Graham Number. The user inputs a stock ticker (e.g., AAPL, MSFT), and the script fetches the necessary data from the Tiingo API to perform the analysis.


## 🚀 Instructions

1. How to run it:

Get stock data from the tinggo api
Ask the user for input
Analyze the data, for example ups and downs and show a graph
Add reccomendations; should the user invest, wait, or not invest



special features

## Who Built It?

Our team (Junyik) built it. 


THis is what is wrong wtih the code. Help me.
Incorrect Endpoint for Fundamental Data:
The fundamentals endpoint might not be available at the URL you're using. Tiingo's /tiingo/fundamentals/{ticker} endpoint may not work as you expect or might require different access.

Fundamentals Data Format:
Even if the fundamentals data is fetched correctly, the structure of the response may not be as expected (e.g., different field names, no metrics data, or missing EPS and Book Value). This could result in your code failing at the metrics.get() part.