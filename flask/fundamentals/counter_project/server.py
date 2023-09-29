from flask import Flask , render_template , redirect , session

app=Flask (__name__)

app.secret_key="vjsvsdlgg,"


@app.route('/')
def count():
    if "count" in session:
        session["count"] += 1  
    else:
        session["count"] = 1  
    return render_template("counter.html")

@app.route('/reset')
def reset():
    session.clear()
    session.pop("count", None) 
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)