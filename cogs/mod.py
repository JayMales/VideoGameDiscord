import discord,aiohttp,aiofiles
from PIL import Image, ImageOps, ImageDraw,ImageFont
from discord.ext import commands

class Mod:

	def __init__(self,bot):
		self.bot = bot
	
	async def on_member_join(self,member):
		# Puts user in default role (needs to be changed so it can be dynamic)
		role = discord.utils.get(member.guild.roles, name="Unity")
		await member.add_roles(role)
		await self._postMyImg(member)
		
	@commands.command(name="welcome", aliases=["img"])
	async def postWelcomeMyImg(self,ctx):
		await self._postMyImg(ctx.author)
	
	async def _postMyImg(self,member):
		# Greats ready to post in first text channel
		public_channel = member.guild.text_channels[0]
		
		# Gets the user's profile picture and saves it.
		async with aiohttp.ClientSession() as session:
			async with session.get(member.avatar_url_as(format="png", size=128)) as resp:
				f = await aiofiles.open('imgs/profilepics/'+str(member.id)+'.png', mode='wb')
				await f.write(await resp.read())
				await f.close()
		
		self._processImg(member)
		
		# Posts the picture in the main chat
		await public_channel.send(file = discord.File(
			"imgs/profilepics/welcomes/"+str(member.id)+"welcomeTemp.png"))
			
	def _processImg(self,member):
		# Opens imgs from user profile and welcome template. Also sets sizes for later
		profilePic = Image.open('imgs/profilepics/'+str(member.id)+'.png').convert('RGBA')
		welcomePic = Image.open('imgs/welcomeTemp.png').convert('RGBA')
		area = (400,10,528,138)
		size = (128, 128)
		
		# Creates a mask for profile pic which is a circle. Then puts the mask on the profilepic
		mask = Image.new('L', size, 0)
		draw = ImageDraw.Draw(mask) 
		draw.ellipse((0, 0) + size, fill=255)
		output = ImageOps.fit(profilePic, mask.size, centering=(0.5, 0.5))
		output.putalpha(mask)
		
		# Puts the profile pic on the welcome pic
		welcomePic.paste(output,area,output)
		
		# Sets fonts
		draw = ImageDraw.Draw(welcomePic)
		font = ImageFont.truetype("font/WELCOME TO THE JUNGLE.ttf", 50)
		
		# Puts the welcome up the top
		x,y =40,20
		draw.text((x, y),"Welcome",(0,103,205),font=font)
		
		# Puts users name and shadow around it down the bottom
		x,y =40,250
		draw.text((x-1, y-1),member.name,(0,0,0),font=font)
		draw.text((x+1, y-1),member.name,(0,0,0),font=font)
		draw.text((x-1, y+1),member.name,(0,0,0),font=font)
		draw.text((x+1, y+1),member.name,(0,0,0),font=font)
		draw.text((x, y),member.name,(0,103,205),font=font)
		
		# Saves the pic
		welcomePic.save("imgs/profilepics/welcomes/"+str(member.id)+"welcomeTemp.png")

def setup(bot):
	bot.add_cog(Mod(bot))