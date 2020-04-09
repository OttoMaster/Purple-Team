#importing sql connector
import mysql.connector

class Database:
#initiliazing the class
	def __init__(self):
		self.__user = 'root'
		self.__password = 'root!1234'
		self.__host = 'localhost'
		self.__schema = 'FedratedInsurance'
#function establish connection
	def createConnection(host,password,username):
		db = mysql.connector.connect(self.__user,self.__password,self.__username,'FedratedInsurance')


