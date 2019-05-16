import requests
from bs4 import BeautifulSoup

link = 'https://vnexpress.net/thoi-su/tong-bi-thu-chu-tich-nuoc-kinh-te-tu-nhan-dang-phat-trien-rat-tot-3924633.html'

res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')
content_div = soup.find(name='div', attrs={'class': 'fck_detail width_common block_ads_connect'})

for p in content_div.find_all(name='p', attrs={'class': 'Normal'}):
    print(p.text)
