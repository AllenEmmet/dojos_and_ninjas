from flask_app.config.mysqlconnections import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojo = None

    @classmethod
    def create_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result

    @classmethod
    def get_ninjas(cls):
        query = 'SELECT * FROM ninjas JOIN dojos ON ninja.dojo_id = dojo.id;'
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        ninjas = []
        for row in results:
            ninja = cls(row)
            dojo_data = {
                'id':row['dojo.id'],
                'name':row['name'],
                'created_at': row['dojo.created_at'],
                'updated_at': row['dojo.updated_at']
            }
            dojo = Dojo(dojo_data)
            ninja.dojo = dojo
            ninjas.append(ninja)
        return ninjas
