from polygon import RESTClient
client = RESTClient(api_key="YmCXRXy_IL8TElP7Z7lzBx5HP58Atf48")

ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_="2023-01-01", to="2023-01-02", limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)
