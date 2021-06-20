import requests


response = requests.get('https://openexchangerates.org/api/currencies.json?app_id=ce7ac8d2d40f4d8e89dc406468b7d302')
print(response.json())
print(response.status_code)
