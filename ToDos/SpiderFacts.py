from actions import Action
from tinydb import Query
import asyncio,random

class SpiderFacts(Action.Action):
	
	def __init__(self,name,command,desc,usage,client,db):
		self.db = db
		self.querys = Query()
		super().__init__(name,command,desc,usage,client)
	
	async def process(self,message):
		rand = random.randint(0, len(self.db.all())-1)
		asyncio.ensure_future(message.channel.send(self.db.search(self.querys.fact.exists())[rand]['fact'], tts=True))