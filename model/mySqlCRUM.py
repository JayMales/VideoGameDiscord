import sqlalchemy as sa
import aiomysql
import asyncio
from aiomysql import create_pool
from key import SQL
from model import user

class Database:
	
	def __init__(self,botto):
		self.botto = botto
		#bot.loop.create_task(check_timers())
		
	async def testing(self):
		bot.sql = yield from aiomysql.connect(host="182.50.132.120", port=3306,user="FarKing",password="KYryZWegSPS42gy",db="Far_discord",loop=botto.loop)
	


########################
# CREATE TABLE IF NOT EXISTS user(userId INT(6) AUTO_INCREMENT PRIMARY KEY, disUserId INT(20), guildId INT(20),schmeckles INT(20),xp INT(20),level INT(10), lastRoll TIMESTAMP) ENGINE=INNODB;
#
# CREATE TABLE IF NOT EXISTS transactions(transId INT(6) AUTO_INCREMENT PRIMARY KEY, payer INT(6) NOT NULL, payee INT(6) NOT NULL, amount INT(20), date TIMESTAMP,
#                           INDEX (payer),
#                           INDEX (payee),
#                           FOREIGN KEY(payer) REFERENCES user(userId) ON DELETE CASCADE,
#                           FOREIGN KEY(payee) REFERENCES user(userId) ON DELETE CASCADE) ENGINE=INNODB;
#                          
# CREATE TABLE IF NOT EXISTS game(gameId INT(6) AUTO_INCREMENT PRIMARY KEY, winner INT(6) NOT NULL, loser INT(6) NOT NULL, type VARCHAR(32), betTotal INT(20), imgLoc VARCHAR(32), date TIMESTAMP, tie  VARCHAR(1),
#                   INDEX (winner),
#                   INDEX (loser),
#                   FOREIGN KEY (winner) REFERENCES user(userId) ON DELETE CASCADE,
#                   FOREIGN KEY (loser) REFERENCES user(userId) ON DELETE CASCADE) ENGINE=INNODB;
#######################