#!/usr/bin/env python3
import requests
import json
import configparser
import os

# Fetch Doge Price
url= "https://sochain.com//api/v2/get_price/DOGE/AUD"
response = requests.get(url)
json_data = json.loads(response.text)

# Parse Data
price = json_data['data']['prices'][0]['price']
floatprice = float(price)

config = configparser.ConfigParser()
if (os.path.exists('config.ini')):
    config.read('config.ini')
else:
    config.read(os.path.dirname(__file__) + os.path.sep + 'config.ini')

wallet_amount = config.get("Config", "coins")
wallet_amount = float(wallet_amount)
purchase_price = config.get("Config", "purchase_price")
purchase_price = float(purchase_price)
investment = wallet_amount * purchase_price
profit = (wallet_amount * floatprice) - investment

def parse_float(profit):
    round_profit = round(profit, 2)
    comma =  "{:,}".format(round_profit)
    final = "$" + comma
    return final

print("So far you have made ", parse_float(profit))
