from actions import Action
import random,discord,asyncio

class Hi(Action.Action):

	async def process(self,message):
		asyncio.ensure_future(message.channel.send(self._hi(), tts=True))
		asyncio.ensure_future(message.channel.send(file = discord.File('imgs/hi.jpg')))
		asyncio.ensure_future(message.channel.send("Yikes!", tts=True))
		
	def _hi(self):
		micheal = "Hey Vsause, Micheal here!"
		rand = random.randint(0, 2)
		if(rand==0):
			micheal = "Hey Micheal, Vsause here!"
		return micheal