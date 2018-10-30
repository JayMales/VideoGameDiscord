import discord,json,asyncio
from discord.ext import commands
import sys, traceback,os
from key import KEY, PREF

public_channel = None

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = PREF

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.template','cogs.memes','cogs.mod','cogs.userManagement']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(f'Failed to load extension {extension}.', file=sys.stderr)
			traceback.print_exc()
	if not os.path.exists("imgs/profilepics/welcomes/"):
		os.makedirs("imgs/profilepics/welcomes/")
			

@bot.event
async def on_ready():
	print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
	# Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
	game = discord.Game("Rewrite Time Boii")
	await bot.change_presence(activity=game)
	print(f'Successfully logged in and booted...!')
	
	
bot.run(KEY, bot=True, reconnect=True)