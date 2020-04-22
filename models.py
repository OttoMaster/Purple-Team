class Department(DB.Model):
    id = DB.Column(DB.Integer,primary_key = True)
    dept_name = DB.Column(DB.String(20),unique = True)

class level(DB.Model):
    id = DB.Column(DB.Integer,primary_key = True)
    level_description = DB.Column(DB.String(20))

class Employee(DB.Model):
    emp_id = DB.Column(DB.Integer,primary_key = True)
    emp_first_name = DB.Column(DB.String(20))
    emp_MI = DB.Column(DB.String(1))
    emp_last_name = DB.Column(DB.String(20))
    emp_salary = DB.Column(DB.Integer)
    emp_title = DB.Column(DB.String(50))


class Supervisor(DB.Model):
    id = DB.Column(DB.Integer,primary_key = True)
    name = DB.Column(DB.String(50))


class PerformanceReviewC(DB.Model):
    id = DB.Column(DB.Integer,primary_key = True)
    first_name = DB.Column(DB.String(20))
    MI = DB.Column(DB.String(1))
    last_name = DB.Column(DB.String(20))
    date_created = DB.Column(DB.DateTime)
    rating_one = DB.Column(DB.String(2))
    rating_two = DB.Column(DB.String(2))
    rating_three = DB.Column(DB.String(2))