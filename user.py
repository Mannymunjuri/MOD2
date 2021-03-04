from flask import Flask,redirect,url_for,render_template, request
from flask.globals import request
app = Flask(__name__)


    
@app.route('/login',methods=['POST'])
def login():
    password = "12345678"
    username = "sam"
    if request.form['username'] != username:
        return render_template("error.html", msg="invalid username")
    
    if request.form['password'] != password:
        return render_template("error.html", msg="invalid password")
    
    return render_template("welcome.html", username = username)


if __name__ == '__main__':
   app.run(debug = True)