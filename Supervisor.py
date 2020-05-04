"""
Author:                     Jai Behl
Date Created:               April 2nd, 2020
Content:                    Supervisor Class
Database:                   MySQL
Programming Language:       Python
"""
# importing dependencies
import mysql.connector

#creating class
class Supervisor:
    #constructor
    def __init__(self,f_name,l_name,emp_id,pos_level):
        self.__f_name = f_name
        self.__l_name = l_name
        self.__emp_id = emp_id
        self.__pos_level = pos_level

    #finding supervisor emp ID
    def getsalary(self, id,table):
        query = ("SELECT * FROM %s "
                 "WHERE POS_LEVEL = %s ")
        cnx = mysql.connector.connect(user='root', database='fed_ins')
        cursor = cnx.cursor(query, table,id)
        results = {"emp_id": "emp_id"}
        for i in cursor:
            results.update({"emp_id": cursor})
        return results
    #view Staff
    def viewStaff(self):
        pass
