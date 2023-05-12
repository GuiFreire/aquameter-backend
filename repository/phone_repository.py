from models.phone import Phone
import databaseConector

class PhoneRepository:
    def create(self, phone:Phone):
        connection = databaseConector.mysqlconnection()
        query = '''
            INSERT INTO phone (Phone, User_id)
            VALUES (%(Phone)s, %(User_id)s) 
        '''
        values = {
            "Phone": phone.phone_number,
            "User_id": phone.user_id,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return phone
    
    def get(self, user_id):
        connection = databaseConector.mysqlconnection()
        query = '''
            SELECT * FROM phone WHERE User_id = %(User_id)s
        '''
        values = {
            "User_id": user_id,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        myresult = cursor.fetchall()
        connection.close()
        return myresult