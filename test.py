from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import pathlib
import string
import random
import json
import re

from module import DataPage
from module import DataGetLinks
from module import ExcelFile



vez='https://vezuviy.su/gotovim-na-vezuvii-ru/'
ever='https://everest-pech.com/pechi-dlya-bani-everest-steam-master-nerzh.-stal-aisi-430/'
etna='https://etna-pech.ru/pechnoe-i-kaminnoe-lite/'
ast='https://aston-pech.ru/katalog/pechi-iz-nerzhaveyushchey-stali-aston/'

hernia = 'eferterterterty5757457'


"""
url = 'https://vezuviy.su/otopitelnoe-oborudovanie/pechi-kaminy/pech-kamin-vezuviy-pk-05-prizmatik-pristennyy-bezh-12-kvt-200-m3-o-150mm/'
req = urllib.request.Request(url)
req = urllib.request.urlopen(req)
html = req.read()
soup = BeautifulSoup(html, 'html.parser')


descrip = str(soup.select('#content_description')[0].div.decode_contents())
print(descrip)
"""

def isLinkCorrect(url):
    domain = r'https://vezuviy.su/|https://everest-pech.com/|https://etna-pech.ru/'
    if re.match(domain, url, re.IGNORECASE):
        return True
    else:
        return False

def isLink(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    if re.match(url_pattern, url):
        return True
    else:
        return False

print(isLink('gdrgrg//http'))