from discord.ext.commands import Bot
from discord.ext import commands

class Action:

	def __init__(self,name,command,desc,client):
		self.name=name
		self.command=command
		self.desc=desc
		self.client=client
	
	def __str__(self):
		return self.name + " does: " + self.desc
		
	def process(self):
		pass