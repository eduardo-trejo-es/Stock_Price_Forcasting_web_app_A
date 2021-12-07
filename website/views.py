from flask import Blueprint, render_template, request, flash
from StockPricePredictionFIles.ForcastingGeneScript import PriceForcaster
from flask import Flask, render_template
from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField


views = Blueprint('views', __name__)
ForcastingObject = PriceForcaster()

class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')

Company_Selected="null"
@views.route('/', methods=['POST', 'GET'])
def home():
    Company_Selected = "null"
    if request.method =='POST':
        try:
            Company_Selected = request.form["TWTR_Val"]
        except:
            pass
        try:
            Company_Selected = request.form["AAPL_Val"]
        except:
            pass          
    else:
        Company_Selected = "null"
    
    form = InfoForm()
    if form.validate_on_submit():
        session['startdate'] = form.startdate.data
        session['enddate'] = form.enddate.data
        #return redirect('date')
    return render_template("home.html", value=ForcastingObject.Gettingforcasting(Company_Selected),form=form)


@views.route('/about')
def about():
    return render_template("about_template.html")