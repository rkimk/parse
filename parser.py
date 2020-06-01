import fake_useragent
import requests, os.path
from bs4 import BeautifulSoup as bs
import browsercookie
ua = fake_useragent.UserAgent()
# ua.update()
user = ua.random

header = {'User-Agent': str(user)}
# proxies = {
#     'http': 'socks5://192.168.1.3:9100',
#     'https': 'socks5://192.168.1.3:9100',
# }

proxies = {
    'http': 'socks5://171.112.94.9:38801',
    'https': 'socks5://171.112.94.9:38801',
}

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



def get_link():
    with open(f'page{single_url[-7:]}.html', 'r', encoding='utf8') as file:
        link = bs(file, 'lxml')
        # print(link)
        ta = link.find_all('a')
        for a in ta:
            print(a)
        # [el.extract() for el in link.select("[style*='border-spacing: 2px;']")]
        # print(link.prettify())
        # print(ta)


        # for b in ta:
        #     print(b)
        # ta = link.find_all('td')
        # for j in ta:
        #     links = j.find('a').get('href')
        # print(links)
        # print(ta)
        # for b in link:
        #     tdd = b.find('href')
        #     print(tdd)

# get_link()

# def getfile(single_url, header, proxies, ipSite, load):
#
#     adress = requests.get(ipSite, headers=header, proxies=proxies)
#     print(header)
#     print(line + "\n[*] IP your network:\n" + adress.text + line)
#     if os.path.exists(f'page{single_url[-7:]}.html'):
#         os.remove(f'page{single_url[-7:]}.html')
#     single_film = session.post(url, headers=header, proxies=proxies, data=load)
#     page = bs(single_film.text, 'lxml')
#     with open(f'page{single_url[-7:]}.html', 'w', encoding='utf8') as f:
#         f.writelines(str(page))


def getfilms(url, header, proxies, load):
    if os.path.exists('nmclub.html'):
        os.remove('nmclub.html')
    with requests.Session() as session:
        content = session.post(url, headers=header, proxies=proxies, data=load)
        cookies = content.cookies

        print(cookies)
        soup = bs(content.text, 'lxml')
        films = []
        find_class_td = soup.find_all('td', attrs={'class': 'genmed'})

        for j in find_class_td:
            link = j.find('a').get('href')
            films.append({
                j.text: link
            })

        # print('Title:' + ' ' + j.text + ' ' + 'Link:' + ' ' + link)

            with open('nmclub.html', 'a', encoding='utf-8') as file:
                file.writelines('\n' + str(j))
            single_url = f"http://nnmclub.to/forum/{link}"
    # print(films)

        # getfile(single_url, header, proxies, ipSite, load)
            print(single_url)
            single_film = session.get(url, headers=header, proxies=proxies, data=load)
            page = bs(single_film.text, 'lxml')
            with open(f'page{single_url[-7:]}.html', 'w', encoding='utf8') as f:
             f.writelines(str(page))
            break

getfilms(url, header, proxies, load)
