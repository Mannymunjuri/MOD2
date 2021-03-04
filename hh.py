from flask import Flask

app=Flask(__name__)

@app.route ("/hello/<int:age>")
def hello_age:
    return "Hello" % age

if __name__ == "__main__":
    app.run()
