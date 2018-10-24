from actions import Action
from imgurpython import ImgurClient
import random

class Meme(Action.Action):
	
	def __init__(self,name,command,desc,client,imgur):
		super().__init__(self,name,command,desc,client)
		self.imgur = imgur

	def process(self):
		ran = 0
		ran = random.randrange(3)
		items = self.imgur.gallery(section='top', sort='time', page=ran, window='week', show_viral=False)
		ran = random.randrange(len(items))
		return items[ran].link