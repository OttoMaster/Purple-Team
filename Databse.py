"""
Author:                     Jai Behl
Date Created:               April 2nd, 2020
Project:                    Fedrated Insurance Salary Charter
Content:                    Database Gateway
Database Engine:            MySQL
Programming Language:       Python
"""
#importing sql connector
import mysql.connector
from mysql.connector import (connection)

# function to connect to database
def Database():
	config = {
		'user': 'root',
		'password': 'root12345!',
		'host': 'localhost',
		'database':'Fedrated_Insurance',
		'raise_on_warnings': True
	}
	cnx = mysql.connector.connect(**config)
	return cnx

Test = Database()
print(Test)

