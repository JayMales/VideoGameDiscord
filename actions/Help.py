from actions import Action
import asyncio

class Help(Action.Action):
	
	def __init__(self,name,command,desc,usage,client,theActions):
		self.theActions = theActions
		super().__init__(name,command,desc,usage,client)
		
	async def process(self,message):
		help = ["Help Menu:"]
		for key in self.theActions:
			help.append(self.theActions[key])
		asyncio.ensure_future(message.channel.send('\n'.join(map(str, help))))