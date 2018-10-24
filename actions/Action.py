from discord.ext.commands import Bot
from discord.ext import commands

class Action:

	def __init__(self,name,command,desc,usage,client):
		self.name=name
		self.command=command
		self.desc=desc
		self.usage=usage
		self.client=client
	
	def __str__(self):
		if self.usage != "":
			format_string = '''s.{}:\n{}\nUsage: s.{} {}\n'''.format(self.command, self.desc,self.command,self.usage)
		else:
			format_string = '''s.{}:\n{}\n'''.format(self.command, self.desc)
		return format_string
		
	def process(self):
		pass