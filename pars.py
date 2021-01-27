import requests
from bs4 import BeautifulSoup
import csv


HOST = 'https://www.avito.ru/bryansk/'
URL = 'https://www.avito.ru/bryansk/rabota?cd=1'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
}
CSV = ()

def get_html(url,params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
html = get_html(URL)
print(html.status_code)