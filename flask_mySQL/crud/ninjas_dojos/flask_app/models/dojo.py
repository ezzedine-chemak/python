from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja
import os

db = os.environ.get("DB")

class Dojo :
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.uptaded_at=data['updated_at']

    @classmethod
    def get_all(cls) :
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL("dojos_and_ninjas_db").query_db(query)
        print("DOJOS--*****----", results)
        dojos = []
        for row in results:
            dojo = cls(row)  
            dojos.append(dojo)
        return dojos


    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_db').query_db(query,data)
        return result

    @classmethod
    def get_ninjas(cls, data: dict) -> list[dict]:
        """
        Retrieves ninjas associated with a specific dojo from the database.

        Args:
            data (dict): A dictionary containing the id of the dojo. Expected keys:
                - 'id': The ID of the dojo.

        Returns:
            list[dict]: A list of dictionaries where each dictionary contains information about a ninja.
        """
        query = "SELECT first_name, last_name, age FROM ninjas LEFT JOIN dojos ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"

        return connectToMySQL(db).query_db(query, data)