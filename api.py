import requests
import json


response = requests.get(
    "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest")
print(response.json())
