import aiosqlite
from model import user

class Database:

	def __init__(self):
		self.dbloc = "model/discordbot.db"
		
	async def selectAllUsers(self):
		return await self.selectManyRows("SELECT * from user")
		
	async def selectAUser(self,currUser):
		result =  await self.__selectAUser(currUser)
		if result is None:
			await self.createUser(currUser)
			result = await self.__selectAUser(currUser)
		return user.User(result)
		
	async def __selectAUser(self, currUser):
		result =  await self.selectOneRow("SELECT * FROM user "+
			"WHERE disUserId = "+str(currUser.id)+" AND guildId = "+
			str(currUser.guild.id)+" LIMIT 1;")
		return result
	
	async def updateSchmeckles(self, currUser, amount, plus):
		async with aiosqlite.connect(self.dbloc) as db:
			cu = await self.selectAUser(currUser)
			if plus:
				cu.schmeckles += amount
			else:
				cu.schmeckles -= amount
				
			await db.execute("UPDATE user SET schmeckles = "+str(cu.schmeckles)+
			" WHERE disUserId = "+str(cu.disUserId)+" AND guildId = "+str(cu.guildId))
			await db.commit()
			
	
	async def createUser(self, currUser):
		async with aiosqlite.connect(self.dbloc) as db:
			if await self.__selectAUser(currUser) is None:
				await db.execute('INSERT INTO user '+
				'(disUserId, guildId,schmeckles,xp,level)'+
				'VALUES('+str(currUser.id)+','+str(currUser.guild.id)+',25,0,1)')
				await db.commit()
				#return await self.selectAUser(currUser)
			
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
# disUserId INTEGER,guildId INTEGER,schmeckles INTEGER,xp INTEGER,level INTEGER, lastRoll real);
#
# CREATE TABLE transactions(transId INTEGER PRIMARY KEY AUTOINCREMENT,payer INTEGER NOT NULL,
# payee INTEGER NOT NULL, amount INTEGER, date REAL,FOREIGN KEY (payer) REFERENCES user(userId),
# FOREIGN KEY(payee) REFERENCES user(userId));
#
# CREATE TABLE game(gameId INTEGER PRIMARY KEY AUTOINCREMENT,winner INTEGER NOT NULL, 
# loser INTEGER NOT NULL, type TEXT, betTotal INTEGER, imgLoc text, date REAL,
# tie INTEGER,FOREIGN KEY (winner) REFERENCES user(userId), FOREIGN KEY(loser) REFERENCES user(userId));
#######################