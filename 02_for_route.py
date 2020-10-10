# Scenario 2:- implement route decorators

from flask import Flask
# Create the obj for start server
app = Flask(__name__)

@app.route('/')
def login_page():
    return "Hello all, i'm developed by flask"


@app.route('/home')
def home_page():
    return "Hello Gopi, i came to home page"


# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True, port=5001)