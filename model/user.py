
class User:

	def __init__(self, tupleUser):
		self.userId, self.disUserId, self.guildId, self.schmeckles, self.xp, self.level = tupleUser
		
# CREATE TABLE user(userId INTEGER PRIMARY KEY AUTOINCREMENT,
# disUserId INTEGER,guildId INTEGER,schmeckles INTEGER,xp INTEGER,level INTEGER);