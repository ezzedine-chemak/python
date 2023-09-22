from flask import Flask 

app = Flask (__name__)
@app.route('/') 

def hello_world ():
    return "hello world !" 

@app.route('/dojo') 
def dojo () :
    return "Dojo !"
 
@app.route('/say/<string:name>') 
def name(name) :
    return f"hi {name}!"

@app.route('/repeat/<int:num>/<string:word>') 
def name_number(word , num) :
    return f"{word * num}!"

if __name__ == "__main__":
    app.run(debug=True)
