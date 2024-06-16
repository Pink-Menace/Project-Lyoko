import discord, random
from random import *
from discord.ext import commands 

class Games(commands.Cog):
  def __init__(self, client):
      self.client = client
      
  @commands.command()
  async def dice(self, ctx):
    one = "You rolled a...**1**!"
    two = "You rolled a...**2**!"
    three = "You rolled a...**3**!"
    four = "You rolled a...**4**!"
    five = "You rolled a...**5**!"
    six = "You rolled a...**6**!"
    foo = [one, two, three, four, five, six]
    embed = discord.Embed(title = 'Dice Roll', description = choice(foo), color = discord.Color.blue(),
    timestamp=ctx.message.created_at)
    embed.set_image(url='https://cdn.discordapp.com/attachments/714675907700457493/768264494706720809/static-assets-upload9010527865714974605.jpg')
    embed.set_author(name='Project Lyoko')
    await ctx.send(embed=embed)
    
  @commands.command()
  async def pp(self, ctx):
    none = "Error 404, you don't have one."
    zero = "8D"
    one = "8=D"
    two = "8==D"
    three = "8===D"
    four = "8====D"
    five = "8=====D"
    six = "8======D"
    seven = "8=======D"
    eight = "8========D"
    nine = "8=========D"
    ten = "8==========D"
    foo = [none, zero, one, two, three, four, five, six, seven, eight, nine, ten]
    embed = discord.Embed(
    title = 'PP',
    description = choice(foo),
    color = discord.Color.blue(),
    timestamp=ctx.message.created_at)
    embed.set_author(name='Project Lyoko')
    await ctx.send(embed=embed)
    
  @commands.command()
  async def rps(self,ctx):
    rock = "You chose rock!"
    paper = "You chose paper!"
    scissors = "You chose scissors!"
    foo = [rock, paper, scissors]
    embed = discord.Embed(color = discord.Color.blue(), 
    title = 'Rock, Paper, Scissors',
    description = choice(foo), timestamp=ctx.message.created_at
    )
    embed.set_author(name='Project Lyoko')
    await ctx.send(embed=embed)
    
  @commands.command()
  async def roulette(self, ctx):
    a = "click"
    b = "click"
    c = "click"
    d = "click"
    e = "click"
    f = "BANG! You were shot"
    foo = [a, b, c, d, e, f]
    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red()
    )
    embed.add_field(name="Russian Roulette", value=choice(foo), inline=False)
    await ctx.send(embed=embed)
    
  @commands.command()
  async def kill (self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    a = "You ran **{0}** over".format(member.name)
    b = "You stabbed **{0}**".format(member.name)
    c = "You scratched **{0}** to death".format(member.name)
    d = "You pushed **{0}** off of a cliff".format(member.name)
    e = "You poured acid on **{0}** and they died".format(member.name)
    f = "A clown car hit **{0}** and they died instantly".format(member.name)
    g = "Donald Trump looked at **{0}** and they died".format(member.name)
    h = "A truck slid and killed **{0}**".format(member.name)
    i = "**{0}** traveled to Atlantis and drowned".format(member.name)
    j = "**{0}** was killed by Poseidon".format(member.name)
    k = "You shoved a dildo sword down **{0}'s** throat and they choke to death".format(member.name)
    l = "**{0}** was impaled by a goat horn".format(member.name)
    m = "**{0}** was killed from over eating".format(member.name)
    n = "**{0}** was decapitated by Jason Voorhees".format(member.name)
    o = "**{0}** was raided by the FBI".format(member.name)
    p = "You electrocute **{0}** with 15,000,000 volts of electricity".format(member.name)
    q = "**{0}** traveled to Ireland and was squashed by a Leprechaun's pot o' gold".format(member.name) 
    r = "You use the Force to siphon the lifeforce from **{0}**".format(member.name)
    s = "**{0}** blasted 80s rock so loud that their head exploded".format(member.name)
    t = "**{0}** was killed by the monster in their closet".format(member.name)
    u = "**{0}** was assassinated by Lee Harvey Oswald".format(member.name)
    v = "**{0}** saw the face of Medusa  and turned to stone".format(member.name)
    w = "**{0}** was cursed by a witch and killed themselves".format(member.name)
    x = "**{0}** was killed by their mom for not doing the dishes".format(member.name)
    y = "**{0}** was mauled to death by a lion".format(member.name)
    z = "**{0}** was cast into the Shadow Realm and got eaten by a Demogorgon".format(member.name)
    foo = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.red()
    )
    embed.add_field(name="**{0}** Was Killed".format(member.name), value=choice(foo), inline=False)
    embed.set_author(name="Project Lyoko")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/714675907700457493/770372413946724352/static-assets-upload9010527865714974605.jpg")
    await ctx.send(embed=embed)
    
  @commands.command()
  async def slap(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    a = f"{ctx.author.mention} has slapped {member.mention}"
    b = f"{ctx.author.mention}'s hand missed {member.mention}"
    foo = (a, b)
    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.red()
    )
    embed.add_field(name="Slap", value=choice(foo))
    embed.set_author(name="Project Lyoko")
    await ctx.send(embed=embed)
    
async def setup(client):
  await client.add_cog(Games(client))
  print("""Cog: Games
Status: Loaded""")