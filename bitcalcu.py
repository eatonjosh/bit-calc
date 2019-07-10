import requests
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print("Mode 1 is for real profit calculations")
print("Mode 2 is for hypophetical profit calculations")
mode = input("Mode 1 or 2?")

if mode == '1':
  original_number = float(input("I brought bitcoin when 1BTC cost:£"))# buy price
elif mode == '2':
    original_number = float(input("If I brought bitcoin when 1BTC cost:£"))
if mode == '1':
    new_number = (r.json()['bpi']['GBP']['rate_float']) # current price
elif mode == '2':
    new_number = float(input("And now 1BTC is worth this:£"))
new_number = round(new_number,2)
increase = new_number - original_number
percentage_increase = increase / original_number * 100
money_invested = float(input("And I invested £"))  # money invested
new_price = money_invested + (money_invested*percentage_increase/100)
new_price = round(new_price,2)
profit = new_price - money_invested
if mode == 1:
    print("It is now be worth: £",new_price)
if mode == 2:
    print("It would now be worth: £",new_price)
print("And that would be £",profit,"profit")
if mode == '1':
    print(new_number," is the current price of BTC")

    
    
   



# python C:\Users\joshe\Documents\bitcalcu.py
