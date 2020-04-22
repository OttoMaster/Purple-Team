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
        job = request.form['job']
        administration = request.form['administration']
        professionalaccountability = request.form['professionalaccountability']
        motivation = request.form['motivation']
        leadership = request.form['leadership']
        result = request.form['result']
        performance_feedback = request.form['performance_feedback']
        # When the user hit submit button
        if form.validate_on_submit():
            employee = Employee()
            emp_id = employee.get_EmpId(first_name,last_name)
            test = employee.printall(first_name,last_name)
            new_review = ReviewDB(first_name,Middle_initial,last_name,job,administration
            ,motivation,leadership,result,performance_feedback)
            db.session.add(new_review)
            db.session.commit()
            flash(f"Review Submited for {form.first_name.data}!", "Success")
            return test
    return render_template('performancereview.html',form = form)

@app.route('/Employee',methods = ['GET'])
def emp_all():
    return 'Hello World'