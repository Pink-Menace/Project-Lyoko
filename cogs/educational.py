import discord, wikipedia, asyncio
from discord.ext import commands

class Educational(commands.Cog):
  def __init__(self, client):
      self.client = client
      
  @commands.command()
  async def addition(self, ctx, x:float, y:float):
    answer = x + y
    await ctx.send(answer)
    
  @commands.command()
  async def subtraction(self, ctx, x:float, y:float):
    answer = x - y
    await ctx.send(answer)
    
  @commands.command()
  async def division(self, ctx, x:float, y:float):
    answer = x / y
    await ctx.send(answer)
    
  @commands.command()
  async def multiply(self, ctx, x:float, y:float):
    answer = x * y
    await ctx.send(answer)
    
  @commands.command()
  async def wiki(self, ctx, *, message=None):
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
    embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
    embed.set_footer(text=f"Created by TheDarkSide#7138")
    embed.add_field(name=f"Searching for {message}", value="Please wait. Searching through wikipedia for your search term")
    await ctx.send(embed=embed, delete_after=0.1)
    try:
      def wiki_page(arg):
        definition = wikipedia.summary(arg, sentences=3, chars=1000, auto_suggest=False)
        link = wikipedia.page(arg, auto_suggest=False, preload=True)
        url = link.url
        return f"""{url}
{definition}"""
      embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
      embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
      embed.set_footer(text=f"Created by TheDarkSide#7138")
      embed.add_field(name=f"Wikipedia Search For: **{message}** from **{ctx.message.author.name}#{ctx.message.author.discriminator}**", value=f"{wiki_page(message)}")
      await ctx.send(embed=embed)
    except wikipedia.exceptions.DisambiguationError:
      embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
      embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
      embed.set_footer(text="Created by TheDarkSide#7138")
      embed.add_field(name=f"Error Looking For: {message}", value=f"Please be more specific in your search terms! Page not found.")
      await ctx.send(embed=embed)
    except wikipedia.exceptions.PageError:
      embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green())
      embed.set_author(name="Project Lyoko", icon_url="https://cdn.discordapp.com/attachments/727396578960343081/798754440475049984/Untitled154_20201119205035.png")
      embed.set_footer(text="Created by TheDarkSide#7138")
      embed.add_field(name=f"Error Looking For: {message}", value=f"Page not found! Please try another search **{ctx.message.author.name}#{ctx.message.author.discriminator}**.")
      await ctx.send(embed=embed)
    
async def setup(client):
  await client.add_cog(Educational(client))
  print("""Cog: Educational
Status: Loaded""")