import discord
from discord.ext import commands

class Mod:

	def __init__(self,bot):
		self.bot = bot
		
	async def on_member_join(member):
		print("New memeber has joined the channel")
		role = discord.utils.get(member.guild.roles, name="Unity")
		await member.add_roles(role)

def setup(bot):
	bot.add_cog(Mod(bot))