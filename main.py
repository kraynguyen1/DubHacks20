import os
import discord
from discord.ext import commands
from discord.utils import get

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

CLIENT = commands.Bot(command_prefix='/')
TOKEN = 'NzY3MTIzNzY1Mjg3OTc2OTgw.X4tVrg.76zyxJjTYwMAmeVnYLJxzGKGbq0'

URL = "https://www.monster.com/jobs/search/?q=Software-Developer\
        &where=Australia"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")





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

# When you type /job
# the bot will list out jobs
@CLIENT.command()
async def job(ctx):
    # Look for Python jobs
    python_jobs = results.find_all("h2", string=lambda t: "python" in t.lower())
    for p_job in python_jobs:
        link = p_job.find("a")["href"]
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")

    # Print out all available jobs from the scraped webpage
    job_elems = results.find_all("section", class_="card-content")

    for job_elem in job_elems:
        title_elem = job_elem.find("h2", class_="title")
        company_elem = job_elem.find("div", class_="company")
        location_elem = job_elem.find("div", class_="location")
        if None in (title_elem, company_elem, location_elem):
            continue
        await ctx.send(title_elem.text.strip())
        await ctx.send(company_elem.text.strip())
        await ctx.send(location_elem.text.strip())


# This method only runs once in the beginning
@CLIENT.event
async def on_ready():
    print("Discord Bot Activated")

# This is testing by Jong
# 12345

# this is testing

CLIENT.run(TOKEN)
