import discord
import typing
from model import databaseCRUM
from discord.ext import commands
from key import PREF


class UserManagement:

	def __init__(self,bot):
		self.bot = bot
		self.db = databaseCRUM.Database()
		
	@commands.command(name="create")
	async def createTheUser(self, ctx):
		user = await self.db.selectAUser(ctx.author)
		await ctx.send("Your id is "+str(user.userId)+" and you have "+
		str(user.schmeckles)+" schmeckles!")
	
	@commands.command(name="balance", aliases=["bal"])
	async def balance(self,ctx,*, member: typing.Optional[discord.Member] = None ):
		if member is None:
			user = await self.db.selectAUser(ctx.author)
			await ctx.send("Your balance is "+
				str(user.schmeckles)+" schmeckles!")
		else:
			user = await self.db.selectAUser(member)
			await ctx.send(member.name+" balance is "+
				str(user.schmeckles)+" schmeckles!")
		
		
	@commands.command(name="pay", aliases=["give"])
	async def pay(self, ctx, member: commands.Greedy[discord.Member], *, amount: int):
		user = await self.db.selectAUser(ctx.author)
		if amount <= 0:
			await ctx.send("Nice try buddy, -10 for you")
			await self.db.updateSchmeckles(ctx.author, 10,False)
		elif user.schmeckles - amount > 0:
			await self.db.updateSchmeckles(ctx.author, amount,False)
			await self.db.updateSchmeckles(member[0], amount,True)
			await ctx.send("You sent "+str(amount)+" to "+member[0].name+".")
		else:
			await ctx.send("You do not have the funds to send that.")
			
	@commands.command(name="adminpay", aliases=["adgive","adpay","admingive"])	
	@commands.is_owner()
	async def adpay(self, ctx, member: commands.Greedy[discord.Member], *, amount: int):
		await self.db.updateSchmeckles(member[0], amount,True)
		await ctx.send(str(amount)+" has been added to "+member[0].name+" account.")
	
	@pay.error
	async def info_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("User not found on this server or invalid amount input. please try again.")
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Missing Args: Should be "+str(PREF[0])+"pay memberName amount.")
	
def setup(bot):
	bot.add_cog(UserManagement(bot))