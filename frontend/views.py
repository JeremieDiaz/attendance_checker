from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#this was supposed to be the route for landing page
@views.route('/')
def home():
    return "<h1>TEST</h1>"