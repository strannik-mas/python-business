import requests
import re

urls = ['https://tinkoff.ru', 'https://alfabank.ru']
tel_regex = r'\+?[78]\s*\d{3}\s*[0-9\-]{7,12}'
for url in urls:
    print('Parse: ', url)
    site_text = requests.get(url).text
    tels = re.findall(tel_regex, site_text)
    print(tels)

