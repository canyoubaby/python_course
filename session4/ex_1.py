import requests

res = requests.get('https://vnexpress.net')
print(res.text)