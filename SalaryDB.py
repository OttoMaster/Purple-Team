#importing database file to create connection
import Database.py

#creating the connection
SalaryDB = createConnection()

#Function to insert in salary table
def insertInto(User):
	cursor = SalaryDB.cursor()
	cursor.execute('Insert into Salary (levelId, levelDesc) VALUES(%s %s) ',User)
	SalaryDB.commit()

#Function to delete data
def deleteData():
	cursor = SalaryDB.cursor()
	cursor.execute('DELETE FROM level where levelId = %s', levelId)
	SalaryDB.commit()