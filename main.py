from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

#use urlOpen
base_url = "https://baike.baidu.com"
history = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + history[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', history[-1])

    sub_url = soup.find_all("a", {"target":"_blank", "href":re.compile("^/item/(%.{2})+$")})

    if len(sub_url) != 0:
        history.append(random.sample(sub_url, 1)[0]['href'])
    else:
        history.pop()


