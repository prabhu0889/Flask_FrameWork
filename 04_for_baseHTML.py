# Scenario 4:- basic of HTML

from flask import Flask

# Create the obj for start server
app = Flask(__name__)


@app.route('/')
def login_page():
    return '''<h1>Hello all, i'm developed by flask<h1>
                <h2>Hello all, i'm developed by flask<h2>
                <h3>Hello all, i'm developed by flask<h3>
                <h4>Hello all, i'm developed by flask<h4>
                <h5>Hello all, i'm developed by flask<h5>
                <h6>Hello all, i'm developed by flask<h6> '''


@app.route('/<name>')  # <string:name>, <int:name>, <path:name>
def home_page(name):
    return f"Hello {name}, i came to home page"


@app.route('/registration')
def registration_page():
    return "Registration page will build soon"


# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True, port=5002)
