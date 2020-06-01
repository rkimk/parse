import urllib.request

from bs4 import BeautifulSoup as bs
import requests, fake_useragent

ua = fake_useragent.UserAgent()
user = ua.random
headers = {'User-Agent': str(user)}
base_url = 'http://nnmclub.to/'
proxies = {'http': 'socks5://192.168.1.3:9050', 'https': 'socks5://192.168.1.3:9050'}


def drop_parse(base_url, headers):




    req = requests.get(base_url, headers=headers, proxies=proxies)
    if req.status_code == 200:
        soup = bs(req.content, 'lxml')
        divs = soup.find_all('div')
        for div in divs:
            print(div)
        with open('file.html', 'w', encoding='utf8') as f:
            f.write(str(divs))
    print(divs)


drop_parse(base_url, headers)