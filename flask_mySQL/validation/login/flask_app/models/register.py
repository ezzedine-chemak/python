from flask_app.config.mysqlconnection import connectToMySQL
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash



class Register():
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.update_at=data['updated_at']

    @classmethod
    def save(cls,data):
        query="INSERT INTO register (first_name,last_name,email,password)VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM register;"
        results = connectToMySQL(cls.db).query_db(query)
        registers = []
        for row in results:
            registers.append( cls(row))
        return registers
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM register WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM register WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        query = "SELECT * FROM register WHERE email = %(email)s;"
        results = connectToMySQL(Register.db).query_db(query,data)
        if len(results) >= 1:
            flash("Email already taken.",)
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!!!",)
            is_valid=False
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters",)
            is_valid= False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters",)
            is_valid= False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters",)
            is_valid= False
        if data['password'] != data['confirm']:
            flash("Passwords don't match",)
        return is_valid