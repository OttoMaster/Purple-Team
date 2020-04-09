

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

	#to get the first name
	def getEmp_fname(self):
		return self.__emp_fname

	#to get the last name
	def getEmp_lname(self):
		return self.__emp_lname

	#to get Employee Id
	def getEmpId(self):
		return self.__emp_ID
		
	#to get employees salary
	def getSalary(self):
		return self.__salary

	def getTitle(self):
		return self.__title

	def getDeptId(self):
		return self.__dept_id

	def getLevelId(self):
		return self.__level_id
