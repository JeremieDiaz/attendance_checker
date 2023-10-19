from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'database_checker'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'email' in session:
        return redirect(url_for('dashboard'))
    return render_template('auth.html', authenticated=False)

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html', email=session['email'])
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT email, password FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user and password == user[1]:
        session['email'] = user[0]
        return redirect(url_for('dashboard'))
    else:
        error = 'Invalid email or password'
        return render_template('auth.html', error=error, authenticated=False)

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cur.fetchone()
    cur.close()

    if existing_user:
        flash('Email already exists. Please use a different email for registration.', 'error')
    elif password != confirm_password:
        flash('Passwords do not match. Please try again.', 'error')
    else:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (email, username, password) VALUES (%s, %s, %s)", (email, username, password))
        mysql.connection.commit()
        cur.close()
        flash('Registration successful! You can now log in.', 'success')

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
