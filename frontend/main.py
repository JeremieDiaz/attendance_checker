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
    return render_template('auth.html', error=None, authenticated=False)

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
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        error = 'Invalid email or password'
        flash(error, 'error')
        return render_template('auth.html', error=error, authenticated=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['passwordConfirm']

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

    return render_template('register.html')

@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'email' in session:
        email = session['email']

        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE email = %s", (email,))
        mysql.connection.commit()
        cur.close()

        session.pop('email', None)
        flash('Your account has been deleted.', 'success')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
