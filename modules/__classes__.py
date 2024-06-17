# -*- coding: utf-8 -*-
import datetime
import discord 
import asyncio
import termcolor
from discord.ext import commands
from termcolor import colored 
from termcolor import cprint 

class __client__:
  def bot():
    client = commands.Bot(command_prefix="$", intents=intents)

class __colors__:
  red = "red"
  blue = "blue"
  green = "green"
  cyan = "cyan"
  grey = "grey"
  yellow = "yellow"
  magenta = "magenta"
  white = "white"
  
class __highlights__:
  grey = "on_grey"
  red = "on_red"
  green = "on_green"
  yellow = "on_yellow"
  blue = "on_blue"
  magenta = "on_magenta"
  cyan = "on_cyan"
  white = "on_white"
  
class __attributes__:
  bold = ["bold"]
  dark = ["dark"]
  underline = ["underline"]
  blink = ["blink"]
  reverse = ["reverse"]
  concealed = ["concealed"]
  
class __time__:
  x = datetime.datetime.now()
  a = (x.strftime("%A"))
  b = (x.strftime("%B"))
  c = (x.strftime("%d"))
  d = (x.strftime("%Y"))
  e = (x.strftime("%I"))
  f = (x.strftime("%M"))
  g = (x.strftime("%S"))
  h = (x.strftime("%p"))
  the_time_is = (a + ", " + b + " " + c + ", " + d + "  " + e + ":" + f + "." + g + " " + h)

class __guilds__:
  async def dm(ctx, *, message=None):
    guild = ctx.guild 
    dm_message = message
    for member in list(guild.members):
      await member.send(f"{dm_message}")
      break
    
class __invite__:
  async def crinvite(ctx):
    author = ctx.message.author
    if author.id == 847466342297632808:
      for guild in client.guilds:
        for channel in guild.channels:
          try:
            if channel.type == discord.ChannelType.voice:
              send_invite = await channel.create_invite(max_uses=100)
              print(f"{guild.name}: {send_invite}")
              break
          except:
            print(f"I can't invite you to {guild.name} since i lack permissions")
    
class __token__:
  TOKEN = "OTE1Njg1MzE4NDA4MTQ3MDE1.G7kepo.4m_lTCMZsgseFZAgEmXwKBUK6hmepnje7nYtg8"
