from actions import Action
import asyncio,random

class Oof(Action.Action):
	
	async def process(self,message):
		ran = random.randrange(30)
		oof ="oof "
		for num in range(0, ran):
			oof = oof +"oof "
		asyncio.ensure_future(message.channel.send(oof, tts=True))