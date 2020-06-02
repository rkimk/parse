import fake_useragent
import requests
from bs4 import BeautifulSoup as bs

ua = fake_useragent.UserAgent()
user = ua.random
session = requests.Session()
header = {'User-Agent': str(user)}

url = 'http://do.rkimk.ru/login/index.php'
login_page = session.get(url, headers=header)
print(login_page.url)
soup = bs(login_page.text, 'html.parser')
token = soup.find('input', dict(name='logintoken'))['value']
data = {
    'anchor':'',
    'logintoken': token,
    'username': '',
    'password': ''
}
auth_page = session.post(login_page.url, headers=header, data=data)
print(auth_page.url)