from models.sensor import Sensor
import databaseConector

class SensorRepository:
    def create(self, sensor:Sensor):
        connection = databaseConector.mysqlconnection()
        query = '''
            INSERT INTO sensor (Sensor_Code, Name, User_id)
            VALUES (%(Sensor_Code)s, %(Name)s, %(User_id)s) 
        '''
        values = {
            "Sensor_Code": sensor.sensor_code,
            "Name": sensor.name,
            "User_id": sensor.user_id
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return sensor
    
    
    def get(self, user_id):
        connection = databaseConector.mysqlconnection()
        query = '''
            SELECT * FROM sensor WHERE user_id = %(user_id)s
        '''
        values = {
            "user_id": user_id,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        myresult = cursor.fetchall()
        connection.close()
        return myresult