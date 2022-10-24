from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import pathlib
import string
import random
import json

from module import DataPage
from module import DataGetLinks
from module import ExcelFile


url = 'https://vezuviy.su/otopitelnoe-oborudovanie/pechi-kaminy/pech-kamin-vezuviy-pk-05-prizmatik-pristennyy-bezh-12-kvt-200-m3-o-150mm/'

req = urllib.request.Request(url)
req = urllib.request.urlopen(req)
html = req.read()
soup = BeautifulSoup(html, 'html.parser')


descrip = str(soup.select('#content_description')[0].div.decode_contents())
print(descrip)