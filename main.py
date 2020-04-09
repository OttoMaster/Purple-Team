from flask import Flask
from flask import render_template
from flask import url_for
from flask_mysql import MySQL

app = Flask(__main__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root12345!'
app.config['MYSQL_DB'] = 'Fed_Insurance'

mysql = MySQL()

mysql.init__app(app)

@app.route('/')
def homepage():
	return render_template('index.html')


@app.route('/DirectorOne')
def DirectorPage:
	return render_template('DirectorPage.html')


@app.route('/DirectorTwo')
def PageTwo():
	return render_template('DirectorTwo')

@app.route('/report',methods=['GET','POST'])
def Report():
	if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Employee(firstName, lastName) VALUES (%s, %s)" %(firstName, lastName))
        mysql.connection.commit()
        cur.close()
	return render_template('Report.html')

if __name__=='__main:
	app.run(debug=true)