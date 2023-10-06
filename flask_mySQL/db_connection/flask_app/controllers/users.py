from flask_app import app
from flask import render_template ,redirect , request 
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    all_users = User.get_all()
    return render_template("index.html",users=all_users)


@app.route('/user/new')
def new():
    return render_template("newusers.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    user.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=user.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    user=user.get_one(data)
    print("USER-----", user.__dict__)
    return render_template("show.html",user=user)


@app.route('/user/update',methods=['POST'])
def update():
    user.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    user.destroy(data)
    return redirect('/users')


