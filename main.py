import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


URL = 'https://www.rbc.ru/'
ua = UserAgent()


def get_html(url, headers={}):
    return requests.get(url, headers=headers).text


def get_news_links(url):
    page = get_html(url, headers={'User-Agent': ua.random})
    soup = BeautifulSoup(page, 'html.parser')
    links = []

    # get first big link
    links.append(soup.find('a', class_='main__big').attrs['href'])
    links_container = soup.find('div', class_='main-feed')

    for link in links_container.find_all('a', class_='main-feed__link'):
        links.append(link.attrs['href'])

    return links
