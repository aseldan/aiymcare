from flask import Flask, render_template, request, url_for
from flask_wtf import csrf
from flask_wtf.csrf import CSRFProtect
import os
from werkzeug.utils import redirect
from wtforms.fields.core import DateField
csrf = CSRFProtect()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ty4425hk54a21eee5719b9s9df7sdfklx'
csrf.init_app(app)

@app.route("/")
def welcome():
    return render_template('welcome.html')

from wtforms import Form, StringField, validators, SubmitField, PasswordField, DateField
from flask_wtf import Form
from wtforms_components import DateRange
from datetime import date, timedelta
#from flask.ext.admin.form.widgets import DatePickerWidget


class RegistrationForm(Form):
    name= StringField('Name', [validators.Length(min=4, max=25)], render_kw={"placeholder":"e.g. Anna"})
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)], render_kw={"placeholder":"e.g. annasmith@gmail.com"})
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    start_date=DateField ("First day of my last period", validators=[DateRange(max=date.today(), min=date.today()-timedelta(days=280))])
    submit = SubmitField('Submit')

@app.route("/signup", methods=["GET","POST"])
def signup():
    form=RegistrationForm()
    if form.validate_on_submit():
        print ("Success")
        print(form.name_first.data, form.email.data)
        return redirect(url_for('feed'))
    return render_template('signup.html', form=form)
    
@app.route("/feed")
def feed():
   
    username= 'Asel'
    week='12'
    return render_template('feed.html', username=username, week=week)