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
try:
    path = r'chromedriver.exe'
except:
    path = "/chromedriver"


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

@CLIENT.command()
async def info(ctx, arg1):
    await ctx.send("Loading stock data...")
    newURL = URL + arg1 +"?p=" + arg1

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Get current price
    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    cur_price_phrase = "Current price of " + arg1 + ": $" + price.text.strip()
    await ctx.send(cur_price_phrase)

    # Get net price
    if (stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
    else:
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
    net_price_phrase = "Net price of " + arg1 + ": $" + (price.text.strip().split()[0])
    await ctx.send(net_price_phrase)

    # Net Percent change in Price
    price = -1
    if(stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
    else:
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
    percent = float(price.text.strip().split()[1].replace('(', '').replace(')', '').replace('%', ''))
    net_percent_change = "Net percent change of " + arg1 + ": " + str(percent) + "%"
    await ctx.send(net_percent_change)

    # Previous Closing Price of stock
    results = soup.find(id="quote-summary")
    pprice = str(results.find('span', {'data-reactid': '98'}).text.strip())
    await ctx.send("Previous Closing Price of " + arg1 + ": $" + pprice)

    oprice = str(results.find('span', {'data-reactid': '103'}).text.strip())
    await ctx.send("Open Price of " + arg1 + ": $" + oprice)

    # Bid Price of stock
    if(results.find('span', {'data-reactid': '108'})):
        bPrice = results.find('span', {'data-reactid': '108'})
    else:
        bPrice = results.find('span', {'data-reactid': '108'})
    if bPrice is not None:
        bPrice = bPrice.text.strip()
        await ctx.send("Bid Price of " + arg1 + ": $" + str(bPrice.split(' x ')[0]))
    else:
        await ctx.send("Bid Price of " + arg1 + ": $0")

    # Day Range
    if(results.find('td', {'data-test': 'DAYS_RANGE-value'})):
        dRStatus = results.find('td', {'data-test': 'DAYS_RANGE-value'})
    else:
        dRStatus = results.find('td', {'data-reactid': '117'})
    await ctx.send("Day Range Status of " + arg1 + ": " + dRStatus.text.strip())

# This method only runs once in the beginning
@CLIENT.event
async def on_ready():
    print("Discord Bot Activated")

# This is testing by Jong
# 12345

# this is testing

CLIENT.run(TOKEN)
