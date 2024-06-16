import discord, aiohttp
from discord import Webhook
from discord.ext import commands

class Webhooks(commands.Cog):
  def __init__(self, client):
      self.client = client

  @commands.command()
  async def weblist(self, ctx):
    guild = ctx.guild
    author = ctx.author
    if author.guild_permissions.manage_webhooks:
      webhook = " ".join([f"{w.name} - {w.url}" for w in await guild.webhooks()])
      await author.send(webhooks)
    else:
      embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
      embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
      embed.set_footer(text=f"Created by _pinkmenace")
      embed.add_field(name="Permissions Error!", value="You do not have permission to use this command!")
      await ctx.send(embed=embed)
    
  @commands.command()
  async def webcreate(self, ctx, *, message=None):
    await ctx.message.delete()
    if message is None: 
      embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
      embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
      embed.set_footer(text=f"Created by _pinkmenace")
      embed.add_field(name="Error!",value=f"{ctx.message.author.name}#{ctx.message.author.discriminator} the webhook name can not be empty!")
      await ctx.send(embed=embed)
    else:
      if ctx.message.author.guild_permissions.manage_webhooks:
        try:
          webhook = await ctx.message.channel.create_webhook(name=message)
          embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
          embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
          embed.set_footer(text=f"Created by _pinkmenace")
          embed.add_field(name="Webhook Creation", value=f"I created {webhook.name} for {ctx.message.author} at {webhook.created_at}")
          await ctx.send(embed=embed)
          await ctx.message.author.send(f"Here's the webhook link {ctx.message.author.name}: {webhook.url} {webhook.id}")
        except:
          await ctx.send("I can only create 10 webhooks per server! Please delete a few webhooks, then use this command again!")
      else:
        ctx.send("You don't have permission to use this command")
      
  @commands.command()
  async def webinfo(self, ctx, *, message=None): 
    webtoken = message
    channel_id = ctx.message.channel.id
    guild = ctx.guild
    webhook = await self.client.fetch_webhook(webtoken)
    if ctx.message.author.guild_permissions.manage_webhooks:
      if message is None:
        await ctx.send("Please enter a webhook id!")
      else:
        embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
        embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
        embed.set_footer(text=f"Created by _pinkmenace")
        embed.add_field(name="Webhook Info", value=f"Information for {webhook.name}")
        embed.add_field(name="Webhook Name", value=f"{webhook.name}")
        embed.add_field(name="Webhook Creation Date", value=f"{webhook.created_at}")
        embed.add_field(name="Webhook Creator", value=f"{webhook.user}")
        embed.add_field(name="Webhook Channel", value=f"{webhook.channel.mention}")
        embed.add_field(name="Webhook Guild ",  value=f"{webhook.guild}")
        await ctx.send(embed=embed)
    else:
      await ctx.send("You don't have permission to user this command!")
    
  @commands.command()
  async def webdelete(self, ctx, *, message=None):
    webtoken = message
    webhook = await self.client.fetch_webhook(webtoken)
    if ctx.message.author.guild_permissions.manage_messages:
      if message is None:
        await ctx.send("ERROR: Please enter the id of the webhook you wish to delete!")
      else:
        await webhook.delete()
        await ctx.send(f"I deleted {webhook.name}")
    else:
      await ctx.send("You don't have permission to use this command!")
    
async def setup(client):
  await client.add_cog(Webhooks(client))
  print("""Cog: Webhooks
Status: Loaded""")