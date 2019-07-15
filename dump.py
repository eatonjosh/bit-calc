import requests
import json
api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=GBP')
api = json.loads(api_request.content)
coins = ["BTC", "BCH", "ETH"]
wanted_coin = input("Wanted coin?")
print(api_request)
print(api)
for x in api:
    for coin in coins:
        if coin == x["symbol"]:
            current_price =
            print(x["name"])
            print(x["price_gbp"])
