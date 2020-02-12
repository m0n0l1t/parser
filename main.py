import requests
import sys
from bs4 import BeautifulSoup
import textwrap
import os
from setting import option

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/69.0', 'accept': '*/*'}


def loop():
    URL = str(sys.argv)
    if len(URL) < 1:
        loop()
    else:
        parse()


def get_html(url):
    session = requests.Session()
    r = session.get(url, headers=HEADERS)
    return r


def save_file(items, path):
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        for item in items:
            try:
                item = item.replace('\n', '`~')

                item = textwrap.fill(item, 80)
                item = item.replace('`~', '\n')
            except:
                pass
            file.write(item)


def reformat(soup, after, before, link_before='', link_after='', link_delete=True, delete=False):
    tmp = ''
    link = ''
    if not link_delete:
        try:
            link = link_before + soup.get('href') + link_after
        except:
            pass
    if not delete:
        tmp = before + soup.get_text() + after + link
    soup.string = tmp
    soup.name = 'content'
    return soup


def reformat_all(soup, after, before, link_before='', link_after='', link_delete=True, delete=False):
    tmp = ''
    for j in soup:
        reformat(j, after, before, link_before, link_after, link_delete, delete)
    return soup


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    name = option['article title']
    heading = option[name]
    first_tag = option['main']
    link = option['a_link']
    items = soup.find(first_tag).parent
    title = ''
    a = soup.find('a').get('href')
    print(a)
    if not heading.delete:
        title = soup.find(name).get_text() + heading.after
    for key, value in option.items():
        link.delete = True
        if key != 'main' and key != 'article title' and key != 'a_link':
            tag = items.find_all(key)
            if key == 'a':
                link.delete = False
            reformat_all(tag, value.after, value.before, link.before, link.after, link.delete, value.delete)


    article = [title]
    article.append(items.get_text())

    return article


def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    end = URL.rfind('/')
    path = os.path.join(os.getcwd(), URL[8:end])
    if not os.path.exists(path):
        os.makedirs(path)
    FILE = URL[end:] + '.txt'
    html = get_html(URL)
    if html.status_code == 200:
        article = get_content(html.text)
        save_file(article, path + FILE)
        try:
            os.startfile(path + FILE)
        except:
            print('Статья была успешно спарсена')
    else:
        print('Error')


if __name__ == '__main__':
    parse()
