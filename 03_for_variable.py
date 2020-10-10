# Scenario 3:- for dynamic value receive from endpoint to route

from flask import Flask
# Create the obj for start server
app = Flask(__name__)

@app.route('/')
def login_page():
    return "Hello all, i'm developed by flask"


@app.route('/<name>')   #<string:name>, <int:name>, <path:name>
def home_page(name):
    return f"Hello {name}, i came to home page"


@app.route('/registration')
def registration_page():
    return "Registration page will build soon"

# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True, port=5002)