import json
import requests


def get_response(url, headers={}):
    return requests.get(url, headers=headers)


def get_body(article):
    body = ''
    for p in article.find_all('p'):
        # get rid of unnecessary content
        if p.find('div') or p.find('script'):
            continue
        body += p.text.strip()

    return body


def write_json(filename, data):
    with open(f'{filename}.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
