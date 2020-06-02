from bs4 import BeautifulSoup as bs
with open('file.html') as file:
    page = bs(file, 'lxml')
    find_div = page.find_all('div', attrs={'class':'postbody'})
    find_span = find_div[0].find_all('span', attrs={'style': 'font-weight: bold'})
    startpos = str(find_div[0]).find(f'{find_span[2]}') + len(f'{find_span[2]}')
    endpos = str(find_div[0]).find('<br/><br/>', startpos)
    print(str(find_div[0])[startpos:endpos].strip())