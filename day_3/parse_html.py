import requests
import bs4

page_text = requests.get('https://auto.ru/').text
# print(page_text)
