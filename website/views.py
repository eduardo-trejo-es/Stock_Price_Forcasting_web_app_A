from flask import Blueprint, render_template, request, flash
from StockPricePredictionFIles.ForcastingGeneScript import PriceForcaster

views = Blueprint('views', __name__)
ForcastingObject = PriceForcaster()

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
                


        #Company_Selected = request.form.get("dropdown_MenuButton")
        #Company_Selected = request.form["dropdown_MenuButton"]
    else:
        Company_Selected = "null"
    return render_template("home.html", value=ForcastingObject.Gettingforcasting(Company_Selected))


@views.route('/about')
def about():
    return render_template("about_template.html")