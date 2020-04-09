#importing Database connection file
import Database.py

#creating a connection
levelDb = Database.createConnection()

# Function to insert data in level table
def insertData(levelUser):
	cursor = levelDb.cursor()
	cursor.execute('Insert into level (levelId, levelDesc) VALUES(%s %s) ',levelUser)
	level.DB.commit()

#Function to delete data from Level table
def deleteData(levelId):
	cursor = levelDb.cursor()
	cursor.execute('DELETE FROM level where levelId = %s', levelId)
	levelDb.commit()

#Function to view all data
def viewData():
	cursor = levelDb.cursor()
	cursor.execute('SELECT LEVELID,LEVELDESC FROM LEVEL')
	levelDb.commit()