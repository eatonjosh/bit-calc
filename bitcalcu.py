import requests
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print("Mode 1 is for real profit calculations")
print("(If I brought BTC when it cost £x, how much would my investment be")
print("worth now?)")

print("Mode 2 is for hypophetical profit calculations")
print("(If I brought BTC when it cost £x, and BTC could be worth £x, how")
print("much would my investment be worth now?)")


mode = input("Mode 1 or 2?")

if mode == '1':
    buy_price = float(input("I brought bitcoin when 1BTC cost:£"))  # original price
    current_price = (r.json()['bpi']['GBP']['rate_float'])  # new number
elif mode == '2':
    buy_price = float(input("If I brought bitcoin when 1BTC cost:£"))
    current_price = float(input("And 1BTC could be worth this:£"))

current_price = round(current_price, 2)
increase = current_price - buy_price
percentage_increase = increase / buy_price * 100
money_invested = float(input("And I invested £"))  # money invested
new_price = money_invested + (money_invested*percentage_increase/100)
new_price = round(new_price, 2)
profit = new_price - money_invested
profit = round(profit, 2)

if mode == '1':
    print("The investment would now be worth: £", new_price)
    print("And the profit would be: £", profit)
    print("£", current_price, " is the current price of BTC")
if mode == '2':
    print("The investment would now be worth: £", new_price)
    print("And that would be £", profit, "profit")
input("")

# python C:\Users\joshe\Documents\bitcalcu.py
