import requests
from bs4 import BeautifulSoup

import json


def get_video_links():
    res = requests.get('http://video.vnexpress.net')
    soup = BeautifulSoup(res.content, 'html.parser')
    list_videos_div = soup.find(name='div', attrs={'class': 'list_video hidden_list width_common'})
    links = list()
