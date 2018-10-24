import discord,json,asyncio,random,datetime
from actions import Meme
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import commands
from tinydb import TinyDB, Query, where
from tinydb.operations import delete,increment
from imgurpython import ImgurClient
from key import KEY,client_id_key, client_secret_key

db = TinyDB('data.json')
users = db.table('User')
querys = Query()
public_channel = None
client_id = client_id_key
client_secret = client_secret_key

imgur = ImgurClient(client_id, client_secret)
client = discord.Client()
bot_prefix= "s."
client = commands.Bot(command_prefix=bot_prefix)
theActions={}

@client.event
async def on_ready():
	print("Bot Online!")
	print('Logged on as {0}!'.format(client))
	if db.all() == []:
		createdb()
		print('Recreated The Database.')
	for cchannel in client.get_all_channels():
		if type(cchannel) == discord.channel.TextChannel:
				global public_channel
				public_channel = cchannel
	theActions["meme"]=Meme.Meme("Meme poster","meme","Posts random memes from imgur",client,imgur)
	
@client.event
async def on_message(message):
	if(message.content.startswith(bot_prefix+"oof")):
		await message.channel.send(oof(), tts=True)
	if(message.content.startswith(bot_prefix+"hi")):
		await message.channel.send(hi(), tts=True)
		await message.channel.send(file = discord.File('hi.jpg'))
		await message.channel.send("Yikes!", tts=True)
	if(message.content.startswith(bot_prefix+"spider")):
		await message.channel.send(facts(), tts=True)
	if(message.content.startswith(bot_prefix+"pick")):
		await message.channel.send(pick(message))
	if(message.content.startswith(bot_prefix+"meme")):
		await message.channel.send(theActions["meme"].process())
	if(message.content.startswith(bot_prefix+"kys")):
		authr = kys(message)
		await authr.create_dm()
		await authr.dm_channel.send("kill yourself")

@client.event
async def on_member_join(member):
	print("New memeber has joined the channel")
	role = discord.utils.get(member.guild.roles, name="Unity")
	await member.add_roles(role)
		
def hi():
	micheal = "Hey Vsause, Micheal here!"
	rand = random.randint(0, 2)
	if(rand==0):
		micheal = "Hey Micheal, Vsause here!"
	return micheal

def pick(msg):
	msg = msg.content
	msg = msg[6:].split(',')
	rand = random.randint(0, len(msg)-1)
	return msg[rand].strip()

def facts():
	rand = random.randint(0, len(db.all())-1)
	print("fact: "+str(rand))
	return db.search(querys.fact.exists())[rand]['fact']

def oof():
	ran = random.randrange(30)
	oof ="oof "
	for num in range(0, ran):
		oof = oof +"oof "
	return oof

def kys(msg):
	authr = msg.author
	for members in msg.channel.members:
		if members.name == msg.content[6:]:
			authr = members
	return authr
	
#@client.listen()
#async def on_member_update(before, after):
#	if after.activity is not None:
#		if(type(after.activity) == discord.activity.Activity):
#			if after.activity.name == 'League of Legends' and after.activity.state == 'In Game':
#				await public_channel.send(after.name +" is playing: "+after.activity.name)
			
def createdb():
	db.insert({'fact':'Spiders can tune the strings in their webs to transmit specific messages.'})
	db.insert({'fact':'Spiders can get high and build different kinds of webs while on weed, caffeine, mescaline and LSD.'})
	db.insert({'fact':'Spiders eat their own webs to recycle them.'})
	db.insert({'fact':'95% of the spiders in your house have never been outside.'})
	db.insert({'fact':'Sometimes thought to be spiders, Daddy Long legs are not spiders. They are not included in the Order Araneae.'})
	db.insert({'fact':'Spiders cant fly but they sometimes sail through the air on a line of silk which is known as ballooning.'})
	db.insert({'fact':'The word spider comes from the old english word spithra and is related to the german spinne both of which mean spinner.'})
	db.insert({'fact':'Wolf spiders can run at speeds of up to two feet per second.'})
	db.insert({'fact':'Some male spiders give dead flies to the females as present.'})
	db.insert({'fact':'Spiders dont sleep all night, instead they take little naps all day and all night. like you and me.'})
	db.insert({'fact':'We think of spiders as solitary creatures, but some  species work together to survive including the african funnelweb spider, which shares its web with hundreds of its brethren.'})
	db.insert({'fact':'Spiders live in burrows underground where it is safe to nap whenever they need to. and others build a little bedroom for themselves on a wall or plant and snuggle up inside.'})
	db.insert({'fact':'The bagheera kiplingi is the worlds only vegetarian spider.'})
	db.insert({'fact':'Spiders have blue blood. in humans, oxygen is bound to hemoglobin, a molecule that contains iron and gives blood its red color. in spiders, oxygen is bound to hemocyanin, a molecule that contains copper rather than iron.'})
	db.insert({'fact':'Triggers besides circadian rhythms and cold temperatures can cause spiders to become unconscious.'})
	db.insert({'fact':'Male spiders weave a small sperm web. They then place a drop of semen on the web, suck it up with their pedipalps, and then use the pedipalp to insert the sperm into the female.'})
	db.insert({'fact':'Arachnids Dont Snore.'})
	db.insert({'fact':'The bite of the Brazilian wandering spider can cause long and painful erections, aswell as other symptoms, in human males.'})
	db.insert({'fact':'A spiders muscles pull its legs inward, but cannot extend its legs out again. Instead, it must pump a watery liquid into its legs to push them out. A dead spiders legs are curled up because there is no fluid to extend the legs again'})
	db.insert({'fact':'Thousands of species of spiders exist around the world. Five thousand jumping spider species are known, and they make up only 13% of spider species.'})
	db.insert({'fact':'Jumping spiders dont have strong muscle legs. They jump by contracting muscles in their abdomen, which forces liquid into their back legs. The back legs then straighten, which catapults the spider forward.'})
	db.insert({'fact':'Spiders have 48 knees.'})

if __name__ == "__main__":
	client.run(KEY)
