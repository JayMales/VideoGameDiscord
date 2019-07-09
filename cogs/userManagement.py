import discord
import typing
from model import databaseCRUM
from discord.ext import commands
from key import PREF
from datetime import datetime, timedelta
import random


class UserManagement(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.db = databaseCRUM.Database()
        #bot.run(self.db2.testing())
		
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
                  
    @commands.command(name="dig", aliases=["Dig"])
    async def dig(self,ctx):
        user = await self.db.selectAUser(ctx.author)
        amount = random.randint(1,25)
        lastRoll = datetime.strptime(user.lastRoll,"%Y-%m-%d %H:%M:%S")
        timenow = datetime.strptime(str(datetime.now())[:-7],"%Y-%m-%d %H:%M:%S")
        if lastRoll > timenow:
            nextRoll = lastRoll - timenow
            nextRoll = divmod(nextRoll.days * 86400 + nextRoll.seconds, 60)
            await ctx.send("Try again in: "+str(nextRoll[0])+" Minutes and "+str(nextRoll[1])+" Seconds.")
            return
        await self.db.updateDig(ctx.author, amount,True)
        await ctx.send("You went digging for some schmeckles and found "+
            str(amount)+" schmeckles!")
		
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
	
    @commands.command(name="createDB", aliases=["createdb"])
    async def createDB(self,ctx):
        await self.db.createDatabase()
        await ctx.send("Created the database if it was created already")
        
    @commands.command(name="adminpay", aliases=["adgive","adpay","admingive"])	
    @commands.is_owner()
    async def adpay(self, ctx, member: commands.Greedy[discord.Member], *, amount: int):
        await self.db.updateSchmeckles(member[0], amount,True)
        await ctx.send(str(amount)+" has been added to "+member[0].name+" account.")

    @adpay.error
    @pay.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found on this server or invalid amount input. please try again.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing Args: Should be "+str(PREF[0])+"pay memberName amount.")
        if isinstance(error, commands.NotOwner):
            await ctx.send("Nice try buddy, -10 for you")
            await self.db.updateSchmeckles(ctx.author, 10,False)
           
	
def setup(bot):
	bot.add_cog(UserManagement(bot))