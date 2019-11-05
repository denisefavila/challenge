import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_soup(url):
    ua = UserAgent()
    r = requests.get(url, headers={'User-Agent': ua.chrome})
    return r.status_code, BeautifulSoup(r.text, 'lxml')