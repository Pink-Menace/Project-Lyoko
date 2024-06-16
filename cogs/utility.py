# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
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

class Utility(commands.Cog):
  def __init__(self, client):
      self.client = client
      
  @commands.command()
  async def time(self, ctx):
    await ctx.message.delete()
    x = datetime.datetime.now()
    a = (x.strftime("%A"))
    b = (x.strftime("%B"))
    c = (x.strftime("%d"))
    d = (x.strftime("%Y"))
    e = (x.strftime("%I"))
    f = (x.strftime("%M"))
    g = (x.strftime("%S"))
    h = (x.strftime("%p"))
    y = (a + ", " + b + " " + c + ", " + d + "  " + e + ":" + f + "." + g + " " + h)
    embed = discord.Embed(
    title = 'Clock',
    description = "It is " + y,
    color = discord.Color.red(), timestamp=ctx.message.created_at)
    embed.set_author(name='Project Lyoko')
    embed.set_image(url='https://cdn.discordapp.com/attachments/714675907700457493/768252975763292170/77f7739f1c9d93ab7779f88f17134674.jpg')
    await ctx.send(embed=embed)
    
  @commands.command()
  async def stats(self, ctx, member: discord.Member):
    channel = ctx.message.channel
    mention = [role.mention for role in member.roles if role.name != '@everyone']
    role_mention = " ".join(mention)
    await ctx.message.delete()
    if member is None:
      embed = discord.Embed(color=discord.Color.blue(), timestamp=ctx.message.created_at)
      embed.add_field(name='Project Lyoko: User Stats', value='Please input a user.', inline=False)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(color= discord.Color.blue(), timestamp=ctx.message.created_at)
      embed.set_author(name = f'Showing Info For {member.name}#{member.discriminator}')
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name='User Name', value="{}".format(member.mention))
      embed.add_field(name = 'User ID', value = "{}".format(member.id),  inline=False) 
      embed.add_field(name = 'User Status', value = "{}".format(member.status), inline=False)
      embed.add_field(name="User Roles", value=f"{role_mention}")
      embed.add_field(name = 'User Join Date', value = "{}".format(member.joined_at), inline= False)
      embed.add_field(name='Account Creation Date', value="{}".format(member.created_at), inline=False)
      await ctx.send(embed=embed)
      
  @commands.command()
  async def server(self, ctx):
    await ctx.message.delete()
    member = discord.Member
    bans = await ctx.guild.bans()
    member_list = f"{member.name}"
    team = ctx.guild
    text_channel_name = ctx.guild.text_channels
    voice_channel_name = ctx.guild.voice_channels
    role_name = [role.mention for role in team.roles if role.name != '@everyone']
    role_mention = " ".join(role_name)
    emojis = len(ctx.guild.emojis)
    mfa = ctx.guild.mfa_level
    contfilter = ctx.guild.explicit_content_filter
    verif = ctx.guild.verification_level
    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.blue())
    embed.set_author(name="Project Lyoko")
    embed.add_field(name="Information For:", value=f"{ctx.message.guild.name}", inline=False)
    embed.add_field(name="Server ID", value= f"{ctx.message.guild.id}", inline=False)
    embed.add_field(name="Server Owner", value =f"{ctx.message.guild.owner.mention}", inline=False)
    embed.add_field(name="Server Members", value=f"{ctx.message.guild.member_count}", inline=False)
    embed.add_field(name="Server Roles", value=f"{len(ctx.guild.roles)} roles", inline=False)
    embed.add_field(name="Server Text Channels", value=f"{len(text_channel_name)} text channels", inline=False)
    embed.add_field(name="Server Voice Channels", value=f"{len(voice_channel_name)} voice channels", inline=False)
    embed.add_field(name="Emojis", value=emojis, inline=False)
    embed.add_field(name="Server Boosts", value=ctx.guild.premium_subscription_count, inline=False)
    embed.add_field(name="Content Filter", value=contfilter, inline=False)
    embed.add_field(name="Verification Level", value=verif, inline=False)
    embed.add_field(name=f"Banned Users In {team.name}", value=f"{len(bans)} banned users", inline=False)
    embed.add_field(name="Server Creation Date", value=f"{ctx.guild.created_at}")
    embed.set_image(url=f"{ctx.message.guild.icon_url}")
    await ctx.send(embed=embed)
    
  @commands.command()
  async def pfp(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(color = discord.Color.red(), timestamp=ctx.message.created_at)
    embed.set_author(name="Project Lyoko")
    embed.add_field(name="Avatar", value="{}'s avatar".format(member.mention))
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed=embed)
    
async def setup(client):
  await client.add_cog(Utility(client))
  print("""Cog: Utility
Status: Loaded""")