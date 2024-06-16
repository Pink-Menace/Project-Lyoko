import json
import discord
from discord.ext import commands 

class Welcome(commands.Cog):
  def __init__(self, client):
      self.client = client
   
  @commands.Cog.listener()
  async def on_member_join(self, member):
    owner = self.client.get_user(847466342297632808)
    channel = member.guild.system_channel
    server = member.guild.name
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_author(name=f"Welcome {member.name}!")
    embed.add_field(name=f"Welcome To {server}", value=f"Please welcome {member.mention} to **{server}**!", inline=False)
    embed.add_field(name="User ID", value=f"{member.id}", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = member.guild.system_channel
    server = member.guild.name
    if channel is not None: 
      embed = discord.Embed(color=discord.Colour.blue())
      embed.set_author(name=f"Goodbye {member.name}")
      embed.add_field(name="Goodbye", value=f"{member.name} left **{server}**! Who needs 'em!", inline=False)
      embed.add_field(name="User ID", value=f"{member.id}", inline=False)
      embed.set_thumbnail(url=member.avatar)
      try:
        await channel.send(embed=embed)
      except:
        pass
  
  @commands.Cog.listener()
  async def on_message(self, message):
    ban_list = [588216939868848130, 434018634067607562, 714221598055596094, 116589185493762052, 695654971131297823, 593996699001946122, 272861784531140609, 476255567309176842, 523567052427100171, 523567052427100171, 484708889133187082, 445123172283580437, 427708371395674136]
    channel = message.channel
    guild = message.guild
    member = message.author
    if member.id in ban_list:
      embed = discord.Embed(color=discord.Colour.blue(), timestamp=message.created_at)
      embed.set_author(name="Project Lyoko")
      embed.add_field(name="Auto Ban", value=f"I banned you, **{message.author.name}#{message.author.discriminator}** because you're in my nuker/raider/cyberbully/pedophile auto ban list. If you believe this is unjustified, or a misunderstanding, please contact _pinkmenace to submit an ID removal request.", inline=False)
      await member.send(embed=embed)
      await member.ban()
      embed = discord.Embed(color=discord.Colour.blue(), timestamp=message.created_at)
      embed.set_author(name="Project Lyoko")
      embed.add_field(name="Auto Ban", value=f"I banned **{message.author.name}#{message.author.discriminator}** because they're in my nuker/raider/cyberbully auto ban list. If you believe this is unjustified, please contact _pinkmenace to submit an ID removal request. Or if you wish to make sure you haven't been added, please contact my developer.", inline=False)
      await channel.send(embed=embed)
  
  @commands.Cog.listener()
  async def on_message(self, message):
    channel = message.channel
    f = open('blacklist.json')
    data = json.load(f)
    for word in data['banned_words']:
      if word in message.content:
        await message.delete()
        embed = discord.Embed(color=discord.Colour.red(), timestamp=message.created_at)
        embed.set_author(name="Project Lyoko")
        embed.add_field(name="Racial Slur Detected", value=f"{message.author.name}#{message.author.discriminator} used a racial slur, so I deleted it.", inline=False)
        embed.add_field(name="User ID", value=f"{message.author.id}", inline=False)
        await channel.send(embed=embed)
      f.close()
  
  @commands.command()
  async def blacklist(self, ctx, message=None):
    if ctx.message.author.id == 847466342297632808:
      file = open("banned_words.txt", "a")
      file.write(f"""
{message}""")
      file.close()
      await ctx.send("passed")
    else:
      await ctx.send("ERROR: Only _pinkmenace can blacklist words or members! Please contact her to have a member/word added!")
      
async def setup(client):
  await client.add_cog(Welcome(client))
  print("""Cog: Welcome
Status: Loaded""")