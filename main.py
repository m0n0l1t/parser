import requests
from bs4 import BeautifulSoup
import textwrap
import os
from setting import option

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/69.0', 'accept': '*/*'}


def get_html(url):
    session = requests.Session()
    r = session.get(url, headers=HEADERS)
    return r


def save_file(items, path):
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        for item in items:
            item = item.replace('\n', '`~')
            item = textwrap.fill(item, 80)
            item = item.replace('`~', '\n')
            file.write(item)


def reformat(soup, after, before, delete=False):
    tmp = ''
    for j in soup:
        if not delete:
            tmp = before+j.get_text()+after
        j.string = tmp
        j.name = 'content'
    return soup


def reformat_link(soup, after, before, link_before, link_after, link_delete=False, delete=False):
    tmp = ''
    link = ''
    for j in soup:
        if not link_delete:
            link = link_before + j.get('href') + link_after
        if not delete:
            tmp = before+j.get_text()+after+link
        j.string = tmp
        j.name = 'content'
    return soup


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    heading = option['h1']
    items = soup.find('p').parent
    link = option['a_link']
    title = ''
    if not heading.delete:
        title = soup.find('h1').get_text()+heading.after
    for key, value in option.items():
        tag = items.find_all(key)
        if key == 'a':
            reformat_link(tag, value.after, value.before, link.before, link.after, link.delete, value.delete)
        else:
            reformat(tag, value.after, value.before, value.delete)

    main = items.find_all('content')
    article = [title]
    for k in main:
        article.append(k.get_text())
    return article


def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    end = URL.rfind('/')
    path = os.path.join(os.getcwd(), URL[8:end])
    if not os.path.exists(path):
        os.makedirs(path)
    FILE = URL[end:]+'.txt'
    html = get_html(URL)
    if html.status_code == 200:
        article = get_content(html.text)
        save_file(article, path+FILE)

        os.startfile(path+FILE)
    else:
        print('Error')


if __name__ == '__main__':
    parse()
