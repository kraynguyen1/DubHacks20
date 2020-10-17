"""
Created on Oct 17 for DUBHACKS20 
ScrapeStocks.py
"""

import requests
import bs4
from bs4 import BeautifulSoup

request = requests.get('https://finance.yahoo.com/quote/FB?p=FB');