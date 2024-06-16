import os 
import sys 
import discord
import discord.utils
from discord.ext import commands 

class Moderation(commands.Cog):
  def __init__(self, client):
      self.client = client
      
  @commands.command()
  async def kick(self, ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
      if member is None:
        embed = discord.Embed(color= discord.Color.red(),
          timestamp=ctx.message.created_at
          )
        embed.add_field(name='Project Lyoko: Kick', value='Please input a user.', inline= False)
        await ctx.send(embed=embed)
      elif member.id == 847466342297632808:
        await ctx.send("I can't ban my owner!")
      else:
        embed = discord.Embed(color = discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name="Project Lyoko")
        embed.add_field(name = "Kick", value=":boot: Get kicked **{}**, from Lyoko".format(member.name), inline=False)
        await ctx.send(embed=embed)
        await member.kick()
    else:
        embed = discord.Embed(color = discord.Color.red(),
          timestamp=ctx.message.created_at)
        embed.add_field(name="Kick", value="You do not have permission to perform this action", inline=False)
        await ctx.send(embed=embed)
        
  @commands.command()
  async def ban(self, ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.ban_members:
      if member is None:
        embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)  
        embed.add_field(name='Project Lyoko: Ban', value='Please input a user.', inline=False)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
        embed.add_field(name='Project Lyoko: Ban', value='**{}** was defeated and returned home in shame'.format(member.name), inline=False)
        await ctx.send(embed=embed)
        await member.ban()
    else:
      embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
      embed.add_field(name='Project Lyoko: Ban', value='You lack permission to perform this action', inline=False)
      await ctx.send(embed=embed)
    
  @commands.command()
  async def warn(self, ctx, member: discord.Member, *, message=None):
    await ctx.message.delete()
    author = ctx.message.author
    if author.guild_permissions.kick_members:
      guild = ctx.message.guild.name
      if member is None:
        embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.red()
        )
        embed.add_field(name="Warning Error", value="Please input a user to warn")
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(timestamp=ctx.message.created_at, color= discord.Color.red()
        )
        embed.set_author(name="Project Lyoko")
        embed.add_field(name=f"{member.name} Has Been Warned By {ctx.message.author.name} For:", value=message)
        embed.add_field(name="Warning Location", value=guild)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.red()
        )
        embed.add_field(name="Warning Error", value="You do not permission to perform this action")
        await ctx.send(embed=embed)
    
  @commands.command()
  async def code_lyoko(self, ctx, amount = 100):
    author = ctx.message.author
    channel = ctx.message.channel
    messages = []
    if author.guild_permissions.ban_members or ctx.message.author.id == 847466342297632808:
      async for message in channel.history(limit=int(amount)):
          messages.append(message)
      await ctx.channel.delete_messages(messages)
      embed = discord.Embed(color = discord.Color.red(), timestamp=ctx.message.created_at)
      embed.add_field(name='Project Lyoko', value='World Reset Successfully', inline= False)
      embed.set_image(url='https://cdn.discordapp.com/attachments/714675907700457493/768264390759284776/kWlSYBl.gif')
      await channel.send(embed=embed)
  
  @commands.command()
  async def mute(self, ctx, member: discord.Member):
    author = ctx.message.author
    if author.guild_permissions.kick_members:
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      guild = ctx.guild
      if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await ctx.send(f"**{member.name}** was muted in **{guild.name}**.")
        for channel in ctx.guild.channels:
          perms2 = channel.overwrites_for(member)
          perms2.send_messages=False
          perms2.speak=False
          await channel.set_permissions(member, overwrite=perms2)
          await member.add_roles(role)
      else:
        await ctx.send(f"**{member.name}** was muted in **{guild.name}**.")
        for channel in ctx.guild.text_channels:
          perms2 = channel.overwrites_for(member)
          perms2.send_messages=False
          perms2.speak=False
          await channel.set_permissions(member, overwrite=perms2)
          await member.add_roles(role)
        
  @commands.command()
  async def unmute(self, ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    author = ctx.message.author
    if author.guild_permissions.kick_members:
      for channel in ctx.guild.channels:
        perms2 = channel.overwrites_for(member)
        perms2.send_messages=True
        perms2.speak=True
        await channel.set_permissions(member, overwrite=perms2)
        await member.remove_roles(role)
      await ctx.send(f"**{member.name}** was unmuted in **{ctx.guild.name}**.")
   
  @commands.command()
  async def renick(self, ctx, member: discord.Member, *, nick, message=None):
    if ctx.message.author.guild_permissions.manage_nicknames:
      await member.edit(nick=nick)
      await member.send("Your nickname was changed in {}".format(ctx.guild.name))
      
async def setup(client):
  await client.add_cog(Moderation(client))
  print("""Cog: Moderation
Status: Loaded""")