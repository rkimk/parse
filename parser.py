import fake_useragent
import requests
from bs4 import BeautifulSoup as bs

ua = fake_useragent.UserAgent()
user = ua.random
header = {'User-Agent': str(user)}
proxies = {
    'http': 'socks5://192.168.1.3:9100',
    'https': 'socks5://192.168.1.3:9100',
}
session = requests.Session()
line = "---------------------------------------------------------------"
ipSite = 'http://icanhazip.com'
adress = requests.get(ipSite, headers=header, proxies=proxies)
start_url = "http://nnmclub.to/forum/tracker.php"
load = {
    'prev_sd': '0',
    'prev_a': '0',
    'prev_my': '0',
    'prev_n': '0',
    'prev_shc': '0',
    'prev_shf': '1',
    'prev_sha': '1',
    'prev_shs': '0',
    'prev_shr': '0',
    'prev_sht': '0',
    'f[]': '954',
    'o': '1',
    's': '2',
    'tm': '-1',
    'shf': '1',
    'sha': '1',
    'ta': '-1',
    'sns': '-1',
    'sds': '-1',
    'nm': '',
    'pn': '',
    'submit': ''}

print(header)
print(line + "\n[*] IP your network:\n" + adress.text + line)

content = session.post(start_url, headers=header, proxies=proxies, data=load)
soup = bs(content.text, 'lxml')
find_class = soup.find_all('a', attrs={'class': 'genmed topictitle'})
for i in find_class:
    print(i)
find_class = soup.find_all('td', attrs={'class': 'genmed'})
for j in find_class:
    print(j)

with open('nmclub.html', 'wb') as file:
    file.writelines(content)
