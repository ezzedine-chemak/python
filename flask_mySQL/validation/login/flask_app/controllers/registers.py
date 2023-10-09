from flask_app import app 
from flask import render_template,redirect,request,session
from flask_app.models.register import Register
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def page_one():
    return render_template('index.html')    

@app.route('/register',methods=['POST'])
def register():

    if not Register.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Register.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

app.route('/login',methods=['POST'])
def login():
    register = Register.get_by_email(request.form)

    if not register:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(register.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['register_id'] = register.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'register_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['register_id']
    }
    return render_template("dashboard.html",register=Register.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')