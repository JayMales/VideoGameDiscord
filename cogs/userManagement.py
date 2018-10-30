import discord
from model import databaseCRUM
from discord.ext import commands


class UserManagement:

	def __init__(self,bot):
		self.bot = bot
		self.db = databaseCRUM.Database()
		
	@commands.command(name="create")
	async def createTheUser(self, ctx):
		user = await self.db.selectAUser(ctx)
		await ctx.send("Your id is "+str(user.userId)+" and you have "+
		str(user.schmeckles)+" schmeckles!")
	
	@commands.command(name="balance", aliases=["bal"])
	async def balance(self,ctx):
		user = await self.db.selectAUser(ctx)
		await ctx.send("Your balance is "+
		str(user.schmeckles)+" schmeckles!")

def setup(bot):
	bot.add_cog(UserManagement(bot))