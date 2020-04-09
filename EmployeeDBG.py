import mysql.connector
import Database.py

class EmployeeDBG(Employee):
#initializing the class
	def __init__(self):
		self.__tablename = 'Employee'


#creating the connection
	def Databaseconnection(self):
		Z = Database.createConnection()
#a function to insert info
	def insertData(User):
		a = Z.cursor()
		a.execute('Insert into Employee (%s %s) VALUES(%s %s) ',User)
		a.commit()