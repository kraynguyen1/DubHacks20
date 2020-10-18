import os
import discord
from discord.ext import commands
from discord.utils import get

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

CLIENT = commands.Bot(command_prefix='/')
TOKEN = 'NzY3MTIzNzY1Mjg3OTc2OTgw.X4tVrg.76zyxJjTYwMAmeVnYLJxzGKGbq0'

URL = 'https://finance.yahoo.com/quote/'

# Get options for chrome and make it headless when testing
# with the console message interupting
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('log-level=3')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('headless')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

# Selenium Driver for Chrome
path = r'chromedriver'

# When you type /ping
# the bot will say "pong!"
@CLIENT.command()
async def ping(ctx):
    await ctx.send("pong!")


# When you type /hello
# the bot will say "hello!"
@CLIENT.command()
async def hello(ctx):
    await ctx.send("hello!")

# When you type /info <stock ticker>
# the bot will return stock data
@CLIENT.command()
async def info(ctx, arg1):
    newURL = URL + arg1 +"?p=" + arg1

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    cur_price_phrase = "Current price of " + arg1 + "is: $" + price.text.strip()
    await ctx.send(cur_price_phrase)

# This method only runs once in the beginning
@CLIENT.event
async def on_ready():
    print("Discord Bot Activated")

# This is testing by Jong
# 12345

# this is testing

CLIENT.run(TOKEN)
