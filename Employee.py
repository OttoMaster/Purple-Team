"""
Author:                     Jai Behl
Date Created:               April 2nd, 2020
Project:                    Fedrated Insurance Salary Charter
Content:                    Employee Class
Database Engine:            MySQL
Programming Language:       Python
"""
#importing dependencies
import mysql.connector
from Databse import Database
#from Employee import Employee
Employee_Database = Database()
#creating the class
class Employee:
	#initializing the class
	def __init__(self,emp_ID,emp_fname,emp_lanme,Salary,title,dept_id,levelId,Supervisor_id):
		self.__emp_ID = emp_ID
		self.__emp_fname = emp_fname
		self.__emp_lname = emp_lanme
		self.__salary = Salary
		self.__title = title
		self.__dept_id = dept_id
		self.__level_id = levelId
		self.__supervisor = Supervisor_id

	#to get Employee Id
	def get_EmpId(self,f_name,l_name):
		mycursor = Employee_Database.cursor()
		sql = "SELECT emp_ID FROM employee WHERE name LIKE %s %s"
		adr = [f_name,l_name]
		mycursor.execute(sql, adr)
		myresult = mycursor.fetchall()
		return myresult

	def getDeptId(self,Dept_Init):
		mycursor = Employee_Database.cursor()
		sql = "SELECT DeptId FROM department WHERE dept_name LIKE %s "
		adr = [Dept_Init]
		mycursor.execute(sql, adr)
		myresult = mycursor.fetchall()
		return myresult

	def getWageClassification(self,emp_id):
		mycursor = Employee_Database.cursor()
		sql = "SELECT Wage_Classification FROM Wage WHERE Emp_id = %s "
		adr = [emp_id]
		mycursor.execute(sql, adr)
		myresult = mycursor.fetchall()
		return myresult
	def printall(self,f_name,l_name):
		return f_name,l_name
