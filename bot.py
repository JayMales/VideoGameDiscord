import discord,json,asyncio,random,datetime
from actions import Meme,Hi,Pick,Oof,SpiderFacts,Help
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
	theActions["meme"]=Meme.Meme("Meme poster","meme","Posts random memes from imgur","",client,imgur)
	theActions["hi"]=Hi.Hi("Say Hi","hi","Posts picture of darcy's face","",client)
	theActions["pick"]=Pick.Pick("Random Pick","pick","Randomly picks 1 of the things you put in.","1,two,three,4",client)
	theActions["oof"]=Oof.Oof("Oof","oof","Says oof a random many amount of time","",client)
	theActions["spider"]=SpiderFacts.SpiderFacts("Spider Facts","spider","Says a spider fact","",client,db)
	theActions["help"]=Help.Help("Help Menu","help","Sends you the help Menu","",client,theActions)
	
@client.event
async def on_message(message):
	if(message.content.startswith(bot_prefix)):
		command = message.content.split(' ')[0]
		command = command.split('.')[1]
		try:
			await theActions[command].process(message)
		except:
			await message.channel.send("command not found")
			await theActions["help"].process(message)
		
	
	#if(message.content.startswith(bot_prefix+"kys")):
	#	authr = kys(message)
	#	await authr.create_dm()
	#	await authr.dm_channel.send("kill yourself")

@client.event
async def on_member_join(member):
	print("New memeber has joined the channel")
	role = discord.utils.get(member.guild.roles, name="Unity")
	await member.add_roles(role)

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
