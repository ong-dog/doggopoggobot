from firebase_dynamic_links import DynamicLinks
import discord
from discord.ext import commands
import asyncio
import functools
import itertools
import math
import random
import youtube_dl
from async_timeout import timeout

bot = commands.Bot(command_prefix='dog.')

apilink = 'https://mc-heads.net/'
api_key = 'AIzaSyCzUyGKiONpSQzMmxsCX7N8zpDCMHfVQfw'
domain = 'moai.page.link'
timeout = 10
dl = DynamicLinks(api_key, domain, timeout) # or DynamicLinks(api_key, domain)
params = {
    "androidInfo": {
        "androidPackageName": 'packagename',
        "androidFallbackLink": 'fallbacklink',
        "androidMinPackageVersionCode": '1'
    },
}


@bot.command()
async def skin(ctx, skin:str):
    await ctx.send(apilink + 'skin' + '/' + skin)

@bot.command()
async def head(ctx, head:str):
    await ctx.send(apilink + 'head' + '/' + head)

@bot.command()
async def body(ctx, body:str):
    await ctx.send(apilink + 'body' + '/' + body)

@bot.command()
async def cape(ctx, cape:str):
    await ctx.send(apilink + 'cape' + '/' + cape)

@bot.command()
async def google(ctx, link:str, aliases=['search', "what's", "Whats", "What is"]):
    link.replace(" ", "+")
    await ctx.send('https://www.letmegooglethat.com/?q=' + link)

@bot.command()
async def link(ctx, link:str):
    short_link = dl.generate_dynamic_link(link, True, params)
    await ctx.send('<' + short_link + '>')

@bot.event  
async def on_ready():
    print('online')
bot.run('ODgyMDI1MzY2NDM1MjkxMTg2.YS1YIg.qajNSS3bVWUl_QKatYptC_EEyNY')
