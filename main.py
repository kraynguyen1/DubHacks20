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

@CLIENT.command()
async def price(ctx, arg1):
    try:
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
    except:
        await ctx.send("Hmmm... Something wrong? :( ")

@CLIENT.command()
async def nprice(ctx, arg1):
    try:
        await ctx.send("Loading stock data...")
        newURL = URL + arg1 +"?p=" + arg1

        driver.get(newURL)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find(id="Lead-3-QuoteHeader-Proxy")
        stock_elems = results.find("div", class_="D(ib) Mend(20px)")
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")

        # Get net price
        if (stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
            price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
        else:
            price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
        net_price_phrase = "Net price of " + arg1 + ": $" + (price.text.strip().split()[0])
        await ctx.send(net_price_phrase)
    except:
        await ctx.send("Hmmm... Something wrong? :( ")

@CLIENT.command()
async def npercent(ctx, arg1):
    try:
        await ctx.send("Loading stock data...")
        newURL = URL + arg1 +"?p=" + arg1

        driver.get(newURL)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find(id="Lead-3-QuoteHeader-Proxy")
        stock_elems = results.find("div", class_="D(ib) Mend(20px)")
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")

        # Get net price
        price = -1
        if(stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
            price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
        else:
            price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
        percent = float(price.text.strip().split()[1].replace('(', '').replace(')', '').replace('%', ''))
        net_percent_change = "Net percent change of " + arg1 + ": " + str(percent) + "%"
        await ctx.send(net_percent_change)
    except:
        await ctx.send("Hmmm... Something wrong? :( ")

# When you type /hello
# the bot will say "hello!"
@CLIENT.command()
async def hello(ctx):
    await ctx.send("hello!")

@CLIENT.command()
async def info(ctx, arg1):
    try:
        await ctx.send("Loading stock data...")
        newURL = URL + arg1 +"?p=" + arg1

        driver.get(newURL)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find(id="quote-summary")

        # Previous Closing Price of stock
        pprice = str(results.find('span', {'data-reactid': '98'}).text.strip())
        await ctx.send("Previous Closing: $" + pprice)
        await ctx.send("-------------------------")
        # Open Price
        oprice = str(results.find('span', {'data-reactid': '103'}).text.strip())
        await ctx.send("Open Price: $" + oprice)
        await ctx.send("-------------------------")

        # Day Range
        if(results.find('td', {'data-test': 'DAYS_RANGE-value'})):
            dRStatus = results.find('td', {'data-test': 'DAYS_RANGE-value'})
        else:
            dRStatus = results.find('td', {'data-reactid': '117'})
        await ctx.send("Day Range: " + dRStatus.text.strip())
        await ctx.send("-------------------------")

        # 52 Week range
        if(results.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})):
            wRStatus = results.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})
        else:
            wRStatus = results.find('td', {'data-reactid': '121'})
        await ctx.send("Week Range: " + wRStatus.text.strip())
        await ctx.send("-------------------------")

        # Volume 
        if(results.find('td', {'data-test': 'TD_VOLUME-value'})):
            VStatus = results.find('td', {'data-test': 'TD_VOLUME-value'})
        else:
            VStatus = results.find('td', {'data-reactid': '125'})
        await ctx.send("Volume: " + VStatus.text.strip())
        await ctx.send("-------------------------")

    except:
        await ctx.send("Hmmm... Something wrong? :( ")

@CLIENT.command()
async def advinfo(ctx, arg1):
    try:
        await ctx.send("Loading stock data...")
        newURL = URL + arg1 +"?p=" + arg1

        driver.get(newURL)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find(id="quote-summary")

        # Bid Price of stock
        if(results.find('span', {'data-reactid': '108'})):
            bPrice = results.find('span', {'data-reactid': '108'})
        else:
            bPrice = results.find('span', {'data-reactid': '108'})
        if bPrice is not None:
            bPrice = bPrice.text.strip()
            await ctx.send("Bid Price: $" + str(bPrice.split(' x ')[0]))
            await ctx.send("-------------------------")
        else:
            await ctx.send("Bid Price: $0")
            await ctx.send("-------------------------")

        # Ask price    
        if(results.find('td', {'data-test': 'ASK-value'})):
            aStatus = results.find('td', {'data-test': 'ASK-value'})
        else:
            aStatus = results.find('td', {'data-reactid': '112'})
        await ctx.send("Ask: " + aStatus.text.strip())
        await ctx.send("-------------------------")

        # Market Cap
        if(results.find('td', {'data-test': 'MARKET_CAP-value'})):
            MCStatus = results.find('td', {'data-test': 'MARKET_CAP-value'})
        else:
            MCStatus = results.find('td', {'data-reactid': '138'})
        await ctx.send("Market Cap: " + MCStatus.text.strip())
        await ctx.send("-------------------------")

        # PE Ratio
        if(results.find('td', {'data-test': 'PE_RATIO-value'})):
            PEStatus = results.find('td', {'data-test': 'PE_RATIO-value'})
        else:
            PEStatus = results.find('td', {'data-reactid': '148'})
        await ctx.send("PE Ratio: " + PEStatus.text.strip())
        await ctx.send("-------------------------")

        # Dividend & yield
        if(results.find('td', {'data-test': 'DIVIDEND_AND_YIELD-value'})):
            DYStatus = results.find('td', {'data-test': 'DIVIDEND_AND_YIELD-value'})
        else:
            DYStatus = results.find('td', {'data-reactid': '163'})
        await ctx.send(" Ratio: " + DYStatus.text.strip())
        await ctx.send("-------------------------")
    except:
        await ctx.send("Hmmm... Something wrong? :( ")

        
        

# This method only runs once in the beginning
@CLIENT.event
async def on_ready():
    print("Discord Bot Activated")

# This is testing by Jong
# 12345

# this is testing

CLIENT.run(TOKEN)
