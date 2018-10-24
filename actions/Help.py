from actions import Action
import asyncio

class Help(Action.Action):
	
	def __init__(self,name,command,desc,usage,client,theActions):
		self.theActions = theActions
		super().__init__(name,command,desc,usage,client)
		
	async def process(self,message):
		authr = message.author
		help = ["Help Menu:"]
		for key in self.theActions:
			help.append(self.theActions[key])
		#asyncio.ensure_future(message.author.create_dm())
		asyncio.ensure_future(message.author.dm_channel.send('\n'.join(map(str, help))))
		#asyncio.ensure_future(message.channel.send("Sent you the help menu, check your dms"))