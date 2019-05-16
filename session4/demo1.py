import requests

res = requests.get('http://google.com')
print(res.text)
print("Check type")
print(type(res))