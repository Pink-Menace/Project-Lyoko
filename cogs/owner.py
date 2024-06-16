import discord, asyncio
from modules import __classes__
from discord.ext import commands

class Owner(commands.Cog):
  def __init__(self, client):
      self.client = client 
 
  @commands.command()
  async def guilds(self, ctx):
    author = ctx.message.author
    guild = ctx.guild
    if author.id == 847466342297632808:
      servers = [f'{guild.name} | {guild.id}' for guild in self.client.guilds]
      guild_list = " \n".join(servers)
      await author.send(guild_list)
    
  @commands.command()
  async def leave(self, ctx, *, message=None):
    author = ctx.message.author
    if author.id == 847466342297632808:
      guild_id = message
      guild = await self.client.get_guild(int(guild_id))
      channel = guild.system_channel
      if channel is not None:
        await channel.send("Leaving this server due to misuse and/or Discord TOS violations! To keep me you must not misuse me or violate Discord's TOS Agreement!")
      else:
        author.send(f"I couldn't send a message to {guild.name}")
      await guild.leave()
    else:
      pass
    
  @commands.command()
  async def glookup(self, ctx, *, message=None):
    author = ctx.message.author
    if author.id == 847466342297632808:
      guild_id = message 
      guild = self.client.get_guild(int(guild_id))
      guild_name = guild.name
      members = guild.member_count
      bans = await guild.bans()
      text_channels = guild.text_channels
      voice_channels = guild.voice_channels
      owner_name = f"{guild.owner.name}#{guild.owner.discriminator}"
      role_name = [role.name for role in guild.roles]
      creation_time = guild.created_at
      info = f"""Guild Name: {guild_name}
Guild ID: {guild.id}
Guild Owner: {owner_name}
Guild Members: {members} members
Guild Roles: {len(role_name)} roles
Bans: {len(bans)} banned members
Text Channels: {len(text_channels)} text channels
Voice Channels: {len(voice_channels)} voice channels
Creation Time: {creation_time}

Info Sent At: {ctx.message.created_at}"""
      await author.send(info)

  @commands.command()
  async def invite(self, ctx, *, message=None):
    author = ctx.message.author 
    guild_id = int(message)
    guild = self.client.get_guild(guild_id)
    if author.id == 847466342297632808:
      for channel in guild.channels:
        try:
          if channel.type == discord.ChannelType.text:
            guild_invite = await channel.create_invite(max_uses=1)
            await author.send(guild_invite)
            break
        except:
            print(f"I don't have permission to create invites in {guild.name}")
    else:
      pass
      print(f"{author.name} tried to use the invite command")
      
  @commands.command()
  async def members(self, ctx, *, message=None):
    guild_id = int(message)
    guild = self.client.get_guild(guild_id)
    author = ctx.message.author
    if author.id == 847466342297632808:
      users = [f'{member.name}#{member.discriminator} | {member.id}' for member in guild.members if member is not member.bot]
      members = " \n".join(users)
      await author.send(members)
    else:
      pass

  @commands.command()
  async def update(self, ctx, *, message=None):
    author = ctx.message.author
    if author.id == 847466342297632808:
      for guild in self.client.guilds:
        channel = guild.system_channel
        try:
          if channel:
            await channel.send(f"Hello {guild.name}. A new update has been added")
            print(f"Message sent to {guild.name} was successful")
            asyncio.sleep(10)
        except:
          print(f"Could not find the system channel in {guild.name}")
    else:
      pass

async def setup(client):
  await client.add_cog(Owner(client))
  print("""Cog: Owner Commands 
Status: Loaded""")