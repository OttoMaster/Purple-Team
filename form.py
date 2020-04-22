"""
Author:                     Jai Behl
Date Created:               April 18th, 2020
Content:                    Forum Structure for performance review
Programming Language:       Python
"""
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField,FieldList,SubmitField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired,Length

class PerformanceReview(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired(),Length(min =2, max = 15)])
    Middle_initial = StringField('M.I',validators=[Length(min = 0, max =1)])
    last_name = StringField('Last Name', validators=[DataRequired(),Length(min =2, max =15)])
    dept = SelectField(
        'Department',validators=[DataRequired()],
        choices=[('IT', 'Information Technology'), ('HR', 'Human Resources'), ('ACC', 'Accounting')]
    )
    administration = SelectField('Administration',validators=[DataRequired()],
                                 choices=[('NI', 'Needs Improvement'), ('SC', 'Successful Contributor'), ('EC', 'Exceptional Contributor')])
    professionalaccountability = SelectField(
        'Professional Accountability',validators=[DataRequired()],
        choices=[('NI', 'Needs Improvement'), ('SC', 'Successful Contributor'), ('EC', 'Exceptional Contributor')]
    )
    motivation = SelectField(
        'Motivation',validators=[DataRequired()],
        choices=[('NI', 'Needs Improvement'), ('SC', 'Successful Contributor'), ('EC', 'Exceptional Contributor')]
    )
    leadership = SelectField(
        'Leadership',validators=[DataRequired()],
        choices=[('NI', 'Needs Improvement'), ('SC', 'Successful Contributor'), ('EC', 'Exceptional Contributor')]
    )
    result = TextAreaField('Results',validators=[DataRequired()])
    performance_feedback = TextAreaField('Performance Feedback',validators=[DataRequired()])
    submit = SubmitField('Submit')

class login(FlaskForm):
    Role = SelectField(
        'Select your role', validators=[DataRequired()],
        choices=[('NI', 'Needs Improvement'), ('SC', 'Successful Contributor'), ('EC', 'Exceptional Contributor')]
    )


