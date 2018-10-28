import discord
from discord.ext import commands


class Template:

	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(name="fuck", aliases=["erh","meme"])
	async def printTest(self, ctx, *, user_input: str):
		
		await ctx.send("this is a test and you sent: "+user_input)

def setup(bot):
	bot.add_cog(Template(bot))