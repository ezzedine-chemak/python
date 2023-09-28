from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def level_one():
    return render_template("check.html",x=4,y=4,color1="blue",color2="aqua")

@app.route('/<int:y>')
def level_two(y):
    return render_template("check.html",x=4,y=y,color1="blue",color2="aqua")

@app.route('/<int:x>/<int:y>')
def level_three(y,x):
    return render_template("check.html",x=x,y=y,color1="blue",color2="aqua")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def level_four(y,x,color1,color2):
    return render_template("check.html",x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)