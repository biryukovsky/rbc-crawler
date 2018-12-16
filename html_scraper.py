import time
from urllib.parse import urlparse
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from utils import get_response, get_body, write_json


MAIN_URL = 'https://www.rbc.ru/'
ua = UserAgent()


def get_news_links(url):
    page = get_response(url, headers={'User-Agent': ua.random}).text
    soup = BeautifulSoup(page, 'html.parser')
    links = []

    # get first big link
    links.append(soup.find('a', class_='main__big').attrs['href'])

    links_container = soup.find('div', class_='main-feed')
    for link in links_container.find_all('a', class_='main-feed__link'):
        links.append(link.attrs['href'])

    return links


def get_news_content(links):
    content = []
    for link in links:
        news_html = get_response(link, headers={'User-Agent': ua.random}).text
        soup = BeautifulSoup(news_html, 'html.parser')
        title = soup.find('div', attrs={
            "class": "article__header"
        }).find('div', attrs={
            "class": "article__header__title"
        }).text.strip()

        article = soup.find('div', class_='article__text')
        body = get_body(article)
        
        path = urlparse(link).path.split('/')
        date = list(filter(lambda e: e.isdigit(), path)) or ''

        content.append({
            "title": title,
            'link': link.split('?', 1)[0],
            "date": '.'.join(date),
            'body': body,
        })

        time.sleep(1)

    return content


if __name__ == '__main__':
    links = get_news_links(MAIN_URL)
    time.sleep(1)
    content = get_news_content(links)
    write_json('html_news', content)
