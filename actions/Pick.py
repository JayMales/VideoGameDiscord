from actions import Action
import asyncio,random

class Pick(Action.Action):
	
	async def process(self,message):
		msg = message.content
		msg = msg[6:].split(',')
		rand = random.randint(0, len(msg)-1)
		asyncio.ensure_future(message.channel.send(str(msg[rand].strip())))