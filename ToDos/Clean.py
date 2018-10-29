from actions import Action
import asyncio

class Clean(Action.Action):
	
	def __init__(self,name,command,desc,usage,client,bot_prefix):
		self.bot_prefix = bot_prefix
		super().__init__(name,command,desc,usage,client)
	
	async def process(self,message):
		asyncio.ensure_future(message.channel.send("Cleaning the channel ;)"))
		async for history in message.channel.history(limit=200):
			if history.content != "Cleaning the channel ;)":
				if history.author == self.client.user:
					asyncio.ensure_future(history.delete())
				if history.content.startswith(self.bot_prefix):
					asyncio.ensure_future(history.delete())
		async for history in message.channel.history(limit=10):
			if history.content == "Cleaning the channel ;)":
				asyncio.ensure_future(history.delete())