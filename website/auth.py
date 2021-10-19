from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/home')
def deleteNotes():
    return render_template('home.html')