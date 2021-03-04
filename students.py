from flask import Flask, render_template
app=Flask (__name__)

@app.route('/students',methods = ['POST', 'GET'])
def student():
   student =["Kamau","John","Mutiso"]
   return render_template ('students.html',  students = student)


if __name__ == '__main__':
   app.run(debug = True)

