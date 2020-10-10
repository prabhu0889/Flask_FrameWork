# Scenario 5:- append HTML

from flask import Flask, render_template

# Create the obj for start server
app = Flask(__name__)


@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/<name>')  # <string:name>, <int:name>, <path:name>
def home_page(name):
    return f"Hello {name}, i came to home page"

@app.route('/registration')
def registration_page():
    return "Registration page will build soon"

# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True, port=5005)
