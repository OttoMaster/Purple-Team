import mysql.connector

class Employee:

  def __init__(self, empid, first_name, last_name):
    self.__empID = empid
    self.__firstName = first_name
    self.__lastName = last_name

  def getid(self, first_name, last_name):
    query = ("SELECT EMP_ID FROM EMPLOYEE "
             "WHERE FIRST_NAME LIKE %s and LAST_NAME LIKE %s")
    cnx = mysql.connector.connect(user='root', database='fed_ins')
    cursor = cnx.cursor(query, first_name, last_name)
    results = {"emp_id" : "emp_id"}
    for i in cursor:
      results.update({"emp_id" : cursor})
    return results

  def getsalary(self, id):
    query = ("SELECT SALARY FROM EMPLOYEE "
             "WHERE EMP_ID = %s ")
    cnx = mysql.connector.connect(user='root', database='fed_ins')
    cursor = cnx.cursor(query, id)
    results = {"emp_id": "emp_id"}
    for i in cursor:
      results.update({"emp_id": cursor})
    return results

  def updatesalary(self):
    pass