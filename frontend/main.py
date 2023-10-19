from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.debug = True

@app.route('/')
def hello():
    return "I'm Online"

# Route for the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle form submission and authentication here
        # Example: Check username and password
        username = request.form['lemail']
        password = request.form['lpassword']
        
        # Add your authentication logic here
        if username == 'your_username' and password == 'your_password':
            # Successful login, redirect to a dashboard or another page
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed, you can display an error message or redirect back to the login page
            return render_template('auth.html', error='Invalid username or password')

    # If it's a GET request, just render the login form
    return render_template('auth.html')

# Dashboard route (for successful login)
@app.route('/dashboard')
def dashboard():
    # Add your dashboard logic here
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run()