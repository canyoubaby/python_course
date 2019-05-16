import requests

res = requests.get('https://vnexpress.net/thoi-su/tong-bi-thu-chu-tich-nuoc-kinh-te-tu-nhan-dang-phat-trien-rat-tot-3924633.html')
print(res.text)