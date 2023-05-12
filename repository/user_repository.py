from models.user import User
import databaseConector

class UserRepository:
    def create(self, user:User):
        connection = databaseConector.mysqlconnection()
        query = '''
            INSERT INTO user (Name, Document, Password)
            VALUES (%(Name)s, %(Document)s, %(Password)s) 
        '''
        values = {
            "Name": user.name,
            "Document": user.document,
            "Password": user.password
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return user

    
    def get(self, id):
        connection = databaseConector.mysqlconnection()
        query = '''
            SELECT * FROM user WHERE ID = %(id)s
        '''
        values = {
            "id": id,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        myresult = cursor.fetchall()
        connection.close()
        return myresult