import discord,random
from discord.ext import commands

class Memes:

	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(name="hi", aliases=["darcy","vsause"])
	async def hiDarcy(self, ctx):
		await ctx.channel.send(self._hi(), tts=True)
		await ctx.channel.send(file = discord.File('imgs/hi.jpg'))
		await ctx.channel.send("Yikes!", tts=True)
	
	@commands.command(name="oof", aliases=["oofs","ooof"])
	async def oof(self, ctx):
		ran = random.randrange(30)
		oof ="oof "
		for num in range(0, ran):
			oof = oof +"oof "
		await ctx.channel.send(oof, tts=True)
		
	def _hi(self):
		micheal = "Hey Vsause, Micheal here!"
		rand = random.randint(0, 2)
		if(rand==0):
			micheal = "Hey Micheal, Vsause here!"
		return micheal

def setup(bot):
	bot.add_cog(Memes(bot))