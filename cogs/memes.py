import discord,random
from discord.voice_client import VoiceClient
from discord.ext import commands

class Memes:
	
	def __init__(self,bot):
		self.bot = bot
		self.imgUrl = "imgs/"
		self.idiots = [["Darcy","hi.jpg"],
			["idk your fucking name but you asked for this","oh_no_booze.jpg"],
			["Fuck yeah","The_gang.jpg"],
			["Mr walker I am","a-a-ron.jpg"],
			["Is that Bruce Lee or Kill Bill","kdog.jpg"]
			]
		
	@commands.command(name="hi", aliases=["darcy","vsause"])
	async def hiDarcy(self, ctx):
		await ctx.channel.send(self._hi(), tts=True)
		await ctx.channel.send(file = discord.File('imgs/hi.jpg'))
		await ctx.channel.send("Yikes!", tts=True)
	
	@commands.command(name="Stupid", aliases=["stupid","idiots"])
	async def randomPicks(self, ctx):
		rand = random.randint(0, len(self.idiots))-1
		await ctx.channel.send(self.idiots[rand][0])
		await ctx.channel.send(file = discord.File(self.imgUrl+self.idiots[rand][1]))
	
	
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

	@commands.command(name="play", aliases=["playme"])
	async def play(self, ctx):	
		channel = ctx.message.author.voice.channel
		voice = await self.bot.join_voice_channel(channel)
		
def setup(bot):
	bot.add_cog(Memes(bot))