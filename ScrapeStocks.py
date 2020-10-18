"""
Created on Oct 17 for DUBHACKS20 
ScrapeStocks.py
"""

import requests
import bs4
from bs4 import BeautifulSoup

def getPrice():
    request = requests.get('https://finance.yahoo.com/quote/FB?p=FB');
    storeSoup = bs4.BeautifulSoup(request.text,"xml");
    price = storeSoup.find_all('div',{c})
