from flask import Flask,redirect,request,url_for
app = Flask(__name__)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return "welcome to post " + username
    else:
        username = request.args.get("username")
        return "welcome to get " + username
        
@app.route('/success')
def success():
    return "success"


if __name__ == '__main__':
   app.run(debug = True)
