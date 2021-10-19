from flask import Blueprint, render_template, request, flash


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user="hello")


@views.route('/about')
def about():
    return render_template("about_template.html")