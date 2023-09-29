from flask import Flask,render_template,request,session,redirect

app=Flask(__name__)

app.secret_key="ezzdin 555 444 111"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/submit', methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['Language']=request.form['Language']
    session['comments']=request.form['comments']
    return redirect('/dispaly_info')

@app.route('/dispaly_info')
def display():
    return render_template("info.html")
    


if __name__=="__main__":
    app.run(debug=True)
