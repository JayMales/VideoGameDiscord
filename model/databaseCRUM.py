import aiosqlite
from model import user

class Database:

	def __init__(self):
		self.dbloc = "model/discordbot.db"
		
	async def selectAllUsers(self):
		return await self.selectManyRows("SELECT * from user")
		
	async def selectAUser(self,ctx):
		result =  await self.__selectAUser(ctx)
		if result is None:
			await self.createUser(ctx)
			result = await self.__selectAUser(ctx)
		return user.User(result)
		
	async def __selectAUser(self, ctx):
		result =  await self.selectOneRow("SELECT * FROM user "+
			"WHERE disUserId = "+str(ctx.author.id)+" AND guildId = "+
			str(ctx.guild.id)+" LIMIT 1;")
		return result
				
	async def createUser(self, ctx):
		async with aiosqlite.connect(self.dbloc) as db:
			if await self.__selectAUser(ctx) is None:
				await db.execute('INSERT INTO user '+
				'(disUserId, guildId,schmeckles,xp,level)'+
				'VALUES('+str(ctx.author.id)+','+str(ctx.guild.id)+',25,0,1)')
				await db.commit()
				#return await self.selectAUser(ctx)
			
	async def selectOneRow(self, query):
		async with aiosqlite.connect(self.dbloc) as db:
			cursor = await db.execute(query)
			row = await cursor.fetchone()
			await cursor.close()
			return row
			
	async def selectManyRows(self, query):
		async with aiosqlite.connect(self.dbloc) as db:
			cursor = await db.execute(query)
			rows = await cursor.fetchall()
			await cursor.close()
			return rows
				
				
				
#######################
# CREATE TABLE user(userId INTEGER PRIMARY KEY AUTOINCREMENT,
# disUserId INTEGER,guildId INTEGER,schmeckles INTEGER,xp INTEGER,level INTEGER);
#
# CREATE TABLE transactions(transId INTEGER PRIMARY KEY AUTOINCREMENT,firstUser INTEGER NOT NULL,
# secondUser INTEGER NOT NULL, amount INTEGER, date REAL,FOREIGN KEY (firstUser) REFERENCES user(userId),
# FOREIGN KEY(secondUser) REFERENCES user(userId));
#
# CREATE TABLE game(gameId INTEGER PRIMARY KEY AUTOINCREMENT,winner INTEGER NOT NULL, 
# loser INTEGER NOT NULL, type TEXT, betTotal INTEGER, imgLoc text, date REAL,
# tie INTEGER,FOREIGN KEY (winner) REFERENCES user(userId), FOREIGN KEY(loser) REFERENCES user(userId));
#######################