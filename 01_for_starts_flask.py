# Scenario 1:- for start the server(werkzeug - WSGI Tool)

from flask import Flask
# Create the obj for start server
app = Flask(__name__)


# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True)