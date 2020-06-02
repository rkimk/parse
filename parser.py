import fake_useragent
import requests, os.path, re
from bs4 import BeautifulSoup as bs

ua = fake_useragent.UserAgent()
user = ua.random
session = requests.Session()
header = {'User-Agent': str(user)}
proxies = {
    'http': 'socks5://192.168.1.3:9100',
    'https': 'socks5://192.168.1.3:9100',
}
# proxies = {
#     'http': 'socks5://171.112.94.9:38801',
#     'https': 'socks5://171.112.94.9:38801',
# }
line = "---------------------------------------------------------------"
ipSite = 'http://icanhazip.com'

url = "http://nnmclub.to/forum/tracker.php"
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


def getfile(download_link, name):
    file = session.get(download_link, proxies=proxies)
    name = name.replace('/', '_')
    name = name.replace(':', '-')
    dir = os.path.abspath('downloads')
    with open(f'{dir}/{name}.torrent', 'wb') as f:
        f.write(file.content)


def getlink(single_url, header, proxies, name):
    single_film = session.get(single_url, headers=header, proxies=proxies)
    page = bs(single_film.text, 'lxml')
    pattern = 'Скачать'
    link = page.find_all('a', text=pattern, attrs={'rel': 'nofollow'})

    for a in link:
        download_link = f'http://nnmclub.to/forum/{str(a["href"])}'
        print('Download_link:' + ' ' + download_link)

        regex = r"\d+,"
        for i in range(0, 18, 2):
            # print(i)
            size = page.find_all('span', attrs={'title': f'Размер блока: {i} MB'})
            for b in size:
                print("Размер торрента составляет: " + re.search(regex, b.get_text()).group(0) + '\n')
                try:
                    filesize = int(re.search(regex, b.get_text()).group(0)[:-1])
                    if filesize <= 15:
                        getfile(download_link, name)

                except AttributeError:
                    print('Not a file')


def getfilms(url, header, proxies, load):
    adress = requests.get(ipSite, headers=header, proxies=proxies)
    print(header)
    print(line + "\n[*] IP your network:\n" + adress.text + line)
    if os.path.exists('nmclub.html'):
        os.remove('nmclub.html')
    content = session.post(url, headers=header, proxies=proxies, data=load)
    soup = bs(content.text, 'lxml')
    films = []
    find_class_td = soup.find_all('td', attrs={'class': 'genmed'})
    for j in find_class_td:
        name = j.text
        link = j.find('a').get('href')
        films.append({
            j.text: link
        })
        print('Title:' + ' ' + j.text + ' ' + 'Link:' + ' ' + link)
        with open('nmclub.html', 'a', encoding='utf-8') as file:
            file.writelines('\n' + str(j))
        single_url = f"http://nnmclub.to/forum/{link}"
        print(single_url)
        getlink(single_url, header, proxies, name)


getfilms(url, header, proxies, load)
