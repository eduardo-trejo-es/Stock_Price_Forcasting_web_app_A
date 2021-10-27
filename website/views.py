from flask import Blueprint, render_template, request, flash
from StockPricePredictionFIles.ForcastingGeneScript import PriceForcaster

views = Blueprint('views', __name__)
ForcastingObject = PriceForcaster()

@views.route('/')
def home():
    return render_template("home.html", value=ForcastingObject.Gettingforcasting())


@views.route('/about')
def about():
    return render_template("about_template.html")