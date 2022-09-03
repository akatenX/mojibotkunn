import discord
from discord.ext import tasks, commands
import asyncio
import requests
import json
import sys
import urllib.request
import socket
import random
import string
import time


mojilist = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","！","？","ぁ","ぃ","ぅ","ぇ","ぉ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","っ","で","ど","な","に","ぬ","ね","の","ば","ぱ","ぴ","び","ぶ","ぷ","ぺ","べ","ぼ","ぽ","ま","み","む","め","も","や","ゃ","ゅ","ゆ","よ","ょ","ら","り","る","れ","ろ","わ","ゎ","を","ん"]



file=open('token.txt')
tokens=file.read()
TOKEN = tokens
file.close()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, help_command=None)

presence = discord.Game(".help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=presence)
    print("login")

@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def help(ctx):
    print("help")
    embed=discord.Embed(title="help", description="文字botのhelpだよ！", color=0xff0000)
    embed.add_field(name="help", value="helpを表示するよ！", inline=True)
    embed.add_field(name="moji3", value="1分ごとにランダムなひらがな3文字を送るよ！", inline=True)
    embed.add_field(name="exit3", value="3mojiを送るのを辞めるよ！", inline=True)
    embed.add_field(name="moji4", value="1分ごとにランダムなひらがな4文字を送るよ！", inline=True)
    embed.add_field(name="exit4", value="4mojiを送るのを辞めるよ！", inline=True)
    embed.add_field(name="moji5", value="1分ごとにランダムなひらがな5文字を送るよ！", inline=True)
    embed.add_field(name="exit5", value="5mojiを送るのを辞めるよ！", inline=True)
    await ctx.send(embed=embed)


mo3size = 0
mo4size = 0
mo5size = 0




@bot.command()
@commands.has_permissions(administrator=True)
async def moji3(ctx):
    global mo3size
    mo3size = 0
    while True:
        await ctx.send(random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist))
        await asyncio.sleep(60)
        if mo3size == 1:
            break



@bot.command()
@commands.has_permissions(administrator=True)
async def exit3(ctx):
    global mo3size
    mo3size = 1
    await ctx.send("終了しました")




@bot.command()
@commands.has_permissions(administrator=True)
async def moji4(ctx):
    global mo4size
    mo4size = 0
    while True:
        await ctx.send(random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist))
        await asyncio.sleep(60)
        if mo4size == 1:
            break



@bot.command()
@commands.has_permissions(administrator=True)
async def exit4(ctx):
    global mo4size
    mo4size = 1
    await ctx.send("終了しました")



@bot.command()
@commands.has_permissions(administrator=True)
async def moji5(ctx):
    global mo5size
    mo5size = 0
    while True:
        await ctx.send(random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist) + random.choice(mojilist))
        await asyncio.sleep(60)
        if mo5size == 1:
            break



@bot.command()
@commands.has_permissions(administrator=True)
async def exit5(ctx):
    global mo5size
    mo5size = 1
    await ctx.send("終了しました")



bot.run(TOKEN)
