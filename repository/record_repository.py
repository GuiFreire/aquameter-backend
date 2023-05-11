from models.record import Record
import databaseConector

class RecordRepository:
    def create(self, record:Record):
        connection = databaseConector.mysqlconnection("xxxx", "xxxx", "xxxx", "xxxx")
        query = '''
            INSERT INTO record (Sensor_Code, Volume, Date)
            VALUES (%(Sensor_Code)s, %(Volume)s, %(Date)s) 
        '''
        values = {
            "Sensor_Code": record.sensor_code,
            "Volume": record.volume,
            "Date": record.date
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return record
    
    def get(self, sensor_code):
        connection = databaseConector.mysqlconnection("xxxx", "xxxx", "xxxx", "xxxx")
        query = '''
            SELECT * FROM record WHERE Sensor_Code = %(sensor_code)s
        '''
        values = {
            "sensor_code": sensor_code,
        }
        cursor = connection.cursor()
        cursor.execute(query, values)
        myresult = cursor.fetchall()
        connection.close()
        return myresult