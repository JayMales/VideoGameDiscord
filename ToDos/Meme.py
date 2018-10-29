from actions import Action
from imgurpython import ImgurClient
import random,asyncio

class Meme(Action.Action):
	
	def __init__(self,name,command,desc,usage,client,imgur):
		self.imgur = imgur
		super().__init__(name,command,desc,usage,client)

	async def process(self,message):
		ran = 0
		ran = random.randrange(3)
		items = self.imgur.gallery(section='top', sort='time', page=ran, window='week', show_viral=False)
		ran = random.randrange(len(items))
		asyncio.ensure_future(message.channel.send(items[ran].link))