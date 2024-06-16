# -*- coding: utf-8 -*-
import os, sys, discord, asyncio, aiohttp, socket, datetime, time, random, requests, logging, json
from modules import __classes__
from discord.ext import commands
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop

intents = discord.Intents.all()
intents.members = True
intents.presences = True
intents.messages = True
language = "en"
__token__ = __classes__.__token__
__time__ = __classes__.__time__

client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')

os.system('clear')

async def load_cogs():
    for file in os.listdir('cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            await client.load_extension(f'cogs.{file[:-3]}')

@loop(seconds=30)
async def presence_change():
  pause = 10
  try:
    await client.change_presence(activity=discord.CustomActivity(name = f"$help | Safeguarding {len(client.guilds)} servers", emoji = None))
    await asyncio.sleep(pause)
  except:
     pass
  try:
    await client.change_presence(activity=discord.CustomActivity(name = "Created by _pinkmenace", emoji = None))
    await asyncio.sleep(pause)
  except:
     pass

@client.event
async def on_ready():
  username = client.user.name
  print(__time__.the_time_is)
  print(f"Logged In As: {username}")
  presence_change.start()
  await load_cogs()
  
@client.command()
async def idban(ctx, *, message=None):
  author = ctx.message.author 
  if author.guild_permissions.ban_members:
    BANNED = await client.fetch_user(int(message))
    await ctx.guild.ban(BANNED, delete_message_days=7)
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.red())
    embed.set_thumbnail(url=BANNED.avatar_url)
    embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
    embed.set_footer(text=f"Created By _pinkmenace")
    embed.add_field(name="ID Ban", value=f"**{BANNED.name}#{BANNED.discriminator}** was banned", inline=False)
    embed.add_field(name="Account Creation Date", value=f"{BANNED.created_at}", inline=False)
    await ctx.send(embed=embed)
  
client.run(__token__.TOKEN)