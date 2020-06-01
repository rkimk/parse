import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import requests, fake_useragent

ua = fake_useragent.UserAgent()
user = ua.random
headers = {'User-Agent': str(user)}
base_url = 'https://www.dropbox.com/s/xedukyjtbpf432p/schedfile.json?dl=0'


def drop_parse(base_url, headers):
    jobs = []
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        divs = soup.find_all('div')
        for div in divs:
            print(div)
        with open('file.html', 'w') as f:
            f.write(str(divs))
    # print(divs)


drop_parse(base_url, headers)