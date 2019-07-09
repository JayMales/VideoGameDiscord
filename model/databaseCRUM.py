import aiosqlite
from model import user
from datetime import datetime, timezone,timedelta

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
            
	async def updateDig(self, currUser, amount, plus):
		theTime = datetime.now() + timedelta(minutes=30)
		timeIn30 = theTime.strftime("%Y-%m-%d %H:%M:%S")
		async with aiosqlite.connect(self.dbloc) as db:
			cu = await self.selectAUser(currUser)
			if plus:
				cu.schmeckles += amount
			else:
				cu.schmeckles -= amount
				
			await db.execute("UPDATE user SET schmeckles = "+str(cu.schmeckles)+
			", lastRoll = '"+timeIn30+"' WHERE disUserId = "+str(cu.disUserId)+" AND guildId = "+str(cu.guildId))
			await db.commit()
			
	
	async def createUser(self, currUser):
		theTime = datetime.now() - timedelta(minutes=35)
		timeIn30 = theTime.strftime("%Y-%m-%d %H:%M:%S")
		print(timeIn30)
		async with aiosqlite.connect(self.dbloc) as db:
			if await self.__selectAUser(currUser) is None:
				await db.execute('INSERT INTO user '+
				'(disUserId, guildId,schmeckles,xp,level,lastRoll)'+
				'VALUES('+str(currUser.id)+','+str(currUser.guild.id)+',25,0,1,"'+timeIn30+'")')
				await db.commit()
				#return await self.selectAUser(currUser) 
                #2004-08-19 18:51:06 %y-%m-%d %H:%M;%S
			
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
			
	async def createDatabase(self):
		async with aiosqlite.connect(self.dbloc) as db:
			await db.execute('create table if not exists user(userId INTEGER PRIMARY KEY AUTOINCREMENT, ' +
                'disUserId INTEGER,guildId INTEGER,schmeckles INTEGER,xp INTEGER,level INTEGER, lastRoll TEXT);')
			await db.commit()
			await db.execute('create table if not exists transactions(transId INTEGER PRIMARY KEY AUTOINCREMENT,payer INTEGER NOT NULL ,'+ 
            'payee INTEGER NOT NULL, amount INTEGER, date TEXT,FOREIGN KEY (payer) REFERENCES user(userId), FOREIGN KEY(payee) REFERENCES user(userId));')

			await db.commit()
			await db.execute('create table if not exists game(gameId INTEGER PRIMARY KEY AUTOINCREMENT,winner INTEGER NOT NULL, loser INTEGER NOT NULL, type TEXT, betTotal INTEGER, imgLoc text, date TEXT, '+
            ' tie INTEGER,FOREIGN KEY (winner) REFERENCES user(userId), FOREIGN KEY(loser) REFERENCES user(userId));')
			await db.commit()
            
#######################
# CREATE TABLE user(userId INTEGER PRIMARY KEY AUTOINCREMENT,
# disUserId INTEGER,guildId INTEGER,schmeckles INTEGER,xp INTEGER,level INTEGER, lastRoll TEXT);
#
# CREATE TABLE transactions(transId INTEGER PRIMARY KEY AUTOINCREMENT,payer INTEGER NOT NULL,
# payee INTEGER NOT NULL, amount INTEGER, date TEXT,FOREIGN KEY (payer) REFERENCES user(userId), FOREIGN KEY(payee) REFERENCES user(userId));
#
# CREATE TABLE game(gameId INTEGER PRIMARY KEY AUTOINCREMENT,winner INTEGER NOT NULL, loser INTEGER NOT NULL, type TEXT, betTotal INTEGER, imgLoc text, date TEXT,
# tie INTEGER,FOREIGN KEY (winner) REFERENCES user(userId), FOREIGN KEY(loser) REFERENCES user(userId));
#
#
######################