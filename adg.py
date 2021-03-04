from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello admin"

@app.route('/guest/<userTyp>')
def hello_guest(userTyp):
    return "Hello "

@app.route('/user/<typ>')
def hello_user(typ):
    if typ == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",userTyp=typ))


if __name__ == '__main__':
   app.run(debug = True)

