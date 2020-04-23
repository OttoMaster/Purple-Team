"""
Author:                     Jai Behl
Date Created:               April 2nd, 2020
Project:                    Fedrated Insurance Salary Charter
Content:                    Flask Restful API
Database Engine:            MySQL
Programming Language:       Python
"""
#importing depedencies
from flask import Flask,render_template,redirect,flash,request
from flask import url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_marshmallow import Marshmallow
from form import PerformanceReview,login
import os

#init application
app = Flask(__name__)
#setting secret key
app.config['SECRET_KEY'] = 'With great powers comes great responsibility'
#identifiying base directory
basedir = os.path.abspath(os.path.dirname(__file__))
#establishing Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
#init database
db = SQLAlchemy(app)
#init marshmallow
ma = Marshmallow(app)

#review class model
class ReviewDB(db.Model):
    id     = db.Column(db.Integer,primary_key = True)
    f_name = db.Column(db.String(15))
    l_name = db.Column(db.String(15))
    job    = db.Column(db.String(2))
    administration   = db.Column(db.String(2))
    professionalaccountability  = db.Column(db.String(2))
    motivation    = db.Column(db.String(2))
    leadership = db.Column(db.String(2))
    result = db.Column(db.String(2))
    performance_feedback = db.Column(db.String(2))
    #Constructor for a Review
    def __init__(self,f_name,l_name,job,administration,professionalaccountability,motivation,leadership,result,performance_feedback):
        self.f_name = f_name
        self.l_name = l_name
        self.job = job
        self.administration   = administration
        self.professionalaccountability  = professionalaccountability
        self.motivation    = motivation
        self.leadership = leadership
        self.result =result
        self.performance_feedback = performance_feedback

#Employee Schema
class Schema(ma.Schema):
    class Meta:
        fields  = ['id','f_name','l_name',
                   'job','administration',
                   'professionalaccountability',
                   'motivation','leadership',
                   'result',
                   'performance_feedback']

#init Schema
Review_Schema = Schema()
Reviews_Schema = Schema(many = True)

#route to home page
@app.route('/')
def home():
    return render_template('homepage.html')

#route to about page
@app.route('/About')
def about():
    form = login()
    return render_template('about page.html',form =form)

#route to form page
@app.route('/review',methods = ['GET','POST'])
def performancereview():
    form = PerformanceReview()
    #getting data from html form
    if request.method == 'POST':
        #requesting data from html form
        first_name = request.form['first_name']
        Middle_initial = request.form['Middle_initial']
        last_name = request.form['last_name']
        dept = request.form['dept']
        administration = request.form['administration']
        professionalaccountability = request.form['professionalaccountability']
        motivation = request.form['motivation']
        leadership = request.form['leadership']
        result = request.form['result']
        performance_feedback = request.form['performance_feedback']
        # When the user hit submit button
        if form.validate_on_submit():
            test = [first_name,last_name]
            new_review = ReviewDB(first_name,Middle_initial,last_name,dept,administration
            ,motivation,leadership,result,performance_feedback)
            db.session.add(new_review)
            db.session.commit()
            flash(f"Review Submited for {form.first_name.data}!", "Success")
            return jsonify(test)
    return render_template('performancereview.html',form = form)
#login page
@app.route('/Employee',methods = ['GET'])
def emp_all():
    all_review = ReviewDB.query.all()
    result = Reviews_Schema.dump(all_review)
    return jsonify(result)


#run server
if __name__ == '__main__':
    app.run(debug =True)