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
login_url = "http://nnmclub.to/forum/login.php"
form = {
    'username': '',
    'password': '',
    'redirect': '',
    'code': '',
    'login': ''
}
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
    name = name.replace('|', '-')
    dir = os.path.abspath('downloads')
    with open(f'{dir}/{name}.torrent', 'wb') as f:
        f.write(file.content)

def genre(page):
    soup = bs(page.text, 'lxml')
    find_div = soup.find_all('div', attrs={'class': 'postbody'})
    find_span = find_div[0].find_all('span', attrs={'style': 'font-weight: bold'})
    startpos = str(find_div[0]).find(f'{find_span[2]}') + len(f'{find_span[2]}')
    endpos = str(find_div[0]).find('<br/><br/>', startpos)
    genre_string = str(find_div[0])[startpos:endpos].strip()
    # print(str(find_div[0])[startpos:endpos].strip())
    return genre_string


def getlink(single_url, header, proxies, name):
    single_film = session.get(single_url, headers=header, proxies=proxies)
    page = bs(single_film.text, 'lxml')
    pattern = 'Скачать'
    link = page.find_all('a', text=pattern, attrs={'rel': 'nofollow'})

    for a in link:
        download_link = f'http://nnmclub.to/forum/{str(a["href"])}'
        print('Download_link:' + ' ' + download_link + '\n' + 'Жанр: ' + genre(single_film))
        regex = r"\d+,"
        for i in range(0, 18, 2):
            # print(i)
            size = page.find_all('span', attrs={'title': f'Размер блока: {i} MB'})
            for b in size:
                print("Размер торрента составляет: " + b.get_text() + '\n')
                try:
                    filesize = int(re.search(regex, b.get_text()).group(0)[:-1])
                    if filesize <= 15:
                        getfile(download_link, name)
                except AttributeError:
                    print('Not a file')


def getfilms(url, header, proxies, load):
    if os.path.exists('nmclub.html'):
        os.remove('nmclub.html')
    adress = requests.get(ipSite, headers=header, proxies=proxies)
    print(header)
    print(line + "\n[*] IP your network:\n" + adress.text + line)
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
        with open('nmclub.html', 'a', encoding='utf-8') as file:
            file.writelines('\n' + str(j.text))
        single_url = f"http://nnmclub.to/forum/{link}"
        print('Title:' + ' ' + j.text + ' ' + 'Link:' + ' ' + single_url)
        getlink(single_url, header, proxies, name)


def login(login_url, header, proxies, form):
    if os.path.exists('auth_nmclub.html'):
        os.remove('auth_nmclub.html')
    login_page = session.post(login_url, headers=header, proxies=proxies, data=form)
    # auth_page = session.post(login_page.url, headers=header, proxies=proxies, data=form)
    with open('auth_nmclub.html', 'a', encoding='utf-8') as file:
        file.writelines('\n' + login_page.text)
    print(login_page.url)
    getfilms(url, header, proxies, load)


login(login_url, header, proxies, form)
