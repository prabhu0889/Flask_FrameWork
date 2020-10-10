# Scenario 5:- append HTML

from flask import Flask, render_template, request
from Learn_DB.TestData import Test_Data
from Learn_DB.DB_Class import Data_Base


# Create the obj for start server
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def login_page():
    alert = ""
    if request.method == "POST":
        uname = request.form.get('USERNAME')   #request.form['USERNAME']
        pwd = request.form.get('PASSWORD')
        print(uname, pwd)
        if uname =="admin" and pwd == "password":
            return render_template('home.html')
        else:
            alert = "invalid Credentials"
            return render_template('login.html', alert = alert)
    return render_template('login.html', alert= alert)

@app.route('/home')  # <string:name>, <int:name>, <path:name>
def home_page():
    return render_template("home.html")

@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    if request.method == "POST":
        f_name = request.form.get('FIRSTNAME')
        email = request.form.get('EMAIL')
        pwd = request.form.get('PASSWORD')
        obj = Test_Data(f_name=f_name, email=email, pwd=pwd)
        con = db.get_connection()
        db.create_table(con, "regist")
        db.insert_records(con, "regist", obj)
        db.close_connection(con)
    return render_template("registration.html")

# Run the server in debug mode
if __name__ == "__main__":
    db = Data_Base('Registration.db')
    app.run(debug=True, port=5028)
