from email.utils import parsedate
import time
from bs4 import BeautifulSoup
from utils import get_response, get_body, write_json

ts = int(time.time())
API_URL = f'https://www.rbc.ru/v8/ajax/mainjson/region/world/?_={ts}'


def get_api_data(url):
    json_response = get_response(url).json()
    output = {}
    for item in json_response['main']['items']:
        pub_date = parsedate(item['publish_date'])
        output[item['fronturl']] = {
            "title": item['title'],
            "publish_date": time.strftime('%d.%m.%Y %H:%M', pub_date)
        }

    return output


def get_news_body(links):
    content = {}
    for link in links:
        news_html = get_response(link).text
        soup = BeautifulSoup(news_html, 'html.parser')
        article = soup.find('div', class_='article__text')
        body = get_body(article)
        content[link] = body
        time.sleep(1)

    return content


def main():
    data = get_api_data(API_URL)
    articles = get_news_body(data.keys())

    for k, v in articles.items():
        data[k]['body'] = v

    write_json('api_news', data)


if __name__ == '__main__':
    main()
