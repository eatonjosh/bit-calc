import requests
import time
url = 'https://api.coinmarketcap.com/v1/ticker/?convert=GBP'
btc_price_gbp = (requests.get(url).json()[0]["price_gbp"])
eth_price_gbp = (requests.get(url).json()[1]["price_gbp"])
bch_price_gbp = (requests.get(url).json()[3]["price_gbp"])


print("Mode 1 is for real profit calculations")
print("(If I brought BTC when it cost £x, how much would my investment be")
print("worth now?)")

print("Mode 2 is for hypophetical profit calculations")
print("(If I brought BTC when it cost £x, and BTC could be worth £x, how")
print("much would my investment be worth now?)")

mode = input("Mode 1 or 2?")
if mode == '1':
    print("")
elif mode == '2':
    print("")
else:
    print("Error: Input 1 or 2")
    time.sleep(3)
    quit()

crypto_choice = input("BTC, BCH or ETH?:")
if crypto_choice == 'BTC' or 'BCH' or 'ETH':
    print("")
else:
    print("Error: Choose BTC, BCH or ETH")
    time.sleep(3)
    quit()

if mode == '1':
    buy_price = float(input("I brought " + crypto_choice + " when 1" + crypto_choice + " cost:£"))  # original price
    if crypto_choice == 'BTC':
        current_price_int = btc_price_gbp  # new number
    elif crypto_choice == 'BCH':
        current_price_int = bch_price_gbp
    elif crypto_choice == 'ETH':
        current_price_int = eth_price_gbp
elif mode == '2':
    buy_price = float(input("I brought " + crypto_choice + " when 1" + crypto_choice + " cost:£"))
    current_price_int = float(input("And 1" + crypto_choice + " could be worth this:£"))

current_price = float(current_price_int)
current_price = round(current_price, 2)
increase = current_price - buy_price
percentage_increase = increase / buy_price * 100

money_invested = float(input("And I invested £"))  # money invested

new_price = money_invested + (money_invested*percentage_increase/100)
new_price = round(new_price, 2)
profit = new_price - money_invested
profit = round(profit, 2)

print("")

if mode == '1':
    print("The investment would now be worth: £", new_price)
    print("And the profit would be: £", profit)
    print("£", current_price, " is the current price of " + crypto_choice)
if mode == '2':
    print("The investment would now be worth: £", new_price)
    print("And that would be £", profit, "profit")
input("")
