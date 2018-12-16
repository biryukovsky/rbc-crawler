# Тестовое задание для РБК

## Описание
Сбор данных с главной страницы [РБК](https://www.rbc.ru/) двумя способами:
  * Парсинг html-страницы с использованием BeautifulSoup (html_scraper.py)
  * Парсинг json-api (api_scraper.py)
Данные записываются в json-файл

## Требования
Python >= 3.6 + requirements.txt

## Запуск
Linux:
```bash
$ virtualenv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
# Для парсинга html:
(venv) $ python html_scraper.py
# Для парсинга api:
(venv) $ python api_scraper.py
```
