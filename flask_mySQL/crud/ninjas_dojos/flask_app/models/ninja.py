from flask_app.config.mysqlconnection import connectToMySQL

class Ninja :
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.uptade_at=data['update_at']
        self.dojo=None

@classmethod
def save(cls,data):
    query = "INSERT INTO ninjas (first_name, last_name,age,dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"
    return connectToMySQL('dojos_and_ninjas_db').query_db(query,data)


