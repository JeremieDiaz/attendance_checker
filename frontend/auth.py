from flask import Blueprint, render_template, request, flash, jsonify
import flask

auth = Blueprint('auth', __name__)

#all of these are yet to be connected to the database.

#these are the routes for login and registration

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth.html")

@auth.route('/logout')
def logout():
    return render_template("auth.html")

#the problem here is i can't render the err/res to the templates using jinja, see if you could fix it?
@auth.route('/sign_up', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('rusername')
        email = request.form.get('remail')
        password = request.form.get('rpassword')
        confirm_password = request.form.get('rconfirm_password')

        if len(email) < 4:
            flash('Email must greater than 3 characters', category='error')
        elif len(username) < 2:
            flash('username must greater than 2 characters', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match', category='error')
        elif len(password) <7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created!', category='success')

        return jsonify(messages=list(flask.get_flashed_messages()))
    return render_template("register.html")