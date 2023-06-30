from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
# Set a secret key for the session
app.secret_key = 'your-secret-key'

@app.route('/')
def home():
    return render_template('index.html')

auth = HTTPBasicAuth()
users = {
    "admin": "password",
    "user": "password"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_password(username, password):
            # Set the session username and redirect to the index page
            session['username'] = username
            return redirect('/')
        else:
            # If the username or password is incorrect, return an error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        # If the request is a GET request, render the login template
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)