# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from discord.ui import Button
import asyncio
import subprocess
import socket
import time
import random
from random import *
import datetime
import logging
import requests
import json
import os 
import sys

class Help(commands.Cog):
  def __init__(self, client):
      self.client = client
      
  @commands.command()
  async def help(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    colour = discord.Colour.blue(), title="Help Menu")
    embed.set_author(name='Project Lyoko', icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
    embed.add_field(name='$moderation', value='Displays administrative commands', inline=False)
    embed.add_field(name='$fun', value='Displays a list of fun commands', inline=False)
    embed.add_field(name="$ascii", value='Displays a list of ascii art commands', inline=False)
    embed.add_field(name='$educational', value='Displays educational commands', inline=False)
    embed.add_field(name="Bot Invite", value="[Invite Me](https://discord.com/oauth2/authorize?client_id=915685318408147015&scope=bot%20applications.commands&permissions=8) | [Support Server](https://discord.gg/k6JdUKC3nX)", inline=False)
    embed.set_footer(text="Created by _pinkmenace")
    await ctx.send(embed=embed)
    
  @commands.command()
  async def fun(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    color = discord.Color.red(),
    timestamp=ctx.message.created_at, 
    title = 'Fun Commands'
    )
    embed.set_author(name='Project Lyoko')
    embed.add_field(name = '$dice', value = 'rolls a die for a random number', inline= False)
    embed.add_field(name = '$pp', value = 'Tells how big your pp is', inline=False)
    embed.add_field(name = '$rps', value = 'Starts a game of rock, paper, scissors', inline=False)
    embed.add_field(name="$roulette", value="Starts a game of Russian Roulette", inline=False)
    embed.add_field(name="$kill", value="Kills the mentioned user", inline=False)
    embed.add_field(name="$slap", value="Slaps the mentioned user", inline=False)
    embed.add_field(name="$time", value="Displays current time (UK)")
    await ctx.send(embed=embed)
      
  @commands.command()
  async def moderation(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.blue())
    embed.set_author(name="Project Lyoko: Admin Commands")
    embed.add_field(name="$warn", value="Warns the mentioned user", inline=False)
    embed.add_field(name="$kick", value="Kicks the mentioned user", inline=False)
    embed.add_field(name="$ban", value="Bans the mentioned user", inline=False)
    embed.add_field(name="$code_lyoko", value="Cleats an X amount of messages", inline=False) 
    embed.add_field(name="$mute", value="Mutes the mentioned user",  inline=False)
    embed.add_field(name="$logout", value="Owner only command. Move along citizen. ", inline=False)
    embed.add_field(name="$renick", value="Changes A User's Nickname", inline=False)
    embed.add_field(name="$server", value="Displays The Server's Information", inline=False)
    embed.add_field(name="$stats", value="Displays The Information Of The Specified User", inline=False)
    await ctx.send(embed=embed)
        
  @commands.command()
  async def educational(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
    embed.set_author(name="Project Lyoko: Educational Commands")
    embed.add_field(name="$addition", value="Adds the given 2 intervals and sends the sum", inline=False)
    embed.add_field(name="$subtraction", value="Subtracts the given 2 intervals and sends the sum", inline=False)
    embed.add_field(name="$multiply", value="Multiplies the 2 given intervals and sends the sum", inline=False)
    embed.add_field(name="$division", value="Divides the 2 given intervals and sends the sum", inline=False)
    embed.add_field(name="$wiki", value="Looks up the specified term on wikipedia")
    await ctx.send(embed=embed)
  
  @commands.command()
  async def ascii(self, ctx):
    embed = discord.Embed(color=discord.Colour.blue(), timestamp=ctx.message.created_at)
    embed.add_field(name="$gnome", value="Sends an ascii gnome", inline=False)
    embed.add_field(name="$reverse", value="Sends an ascii Uno Reverse Card", inline=False)
    await ctx.send(embed=embed)
      
async def setup(client):
  await client.add_cog(Help(client))
  print("""Cog: Help
Status: Loaded""")