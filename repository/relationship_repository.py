from models.relationship import RelationShip
import databaseConector

class RelationshipRepository:
    def create(self, relationship:RelationShip):
        connection = databaseConector.mysqlconnection()
        query = '''
            INSERT INTO relationship (User_id, Parent_User_ID, User_Sensor_Code)
            VALUES (%(User_id)s, %(Parent_User_ID)s, %(User_Sensor_Code)s) 
        '''
        values = {
            "User_id": relationship.user_id,
            "Parent_User_ID": relationship.parent_user_id,
            "User_Sensor_Code": relationship.user_sensor_code
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return relationship
    
    def get(self, parent_user_id):
        connection = databaseConector.mysqlconnection()
        query = '''
            SELECT * FROM relationship WHERE Parent_User_ID = %(Parent_User_ID)s
        '''
        values = {
            "Parent_User_ID": parent_user_id,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        myresult = cursor.fetchall()
        connection.close()
        return myresult