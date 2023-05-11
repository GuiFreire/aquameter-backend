from models.sensor import Sensor
import csv

class SensorRepository:
    def create(self, sensor:Sensor):
        with open('./repository/sensor.csv', "a") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([sensor.name, sensor.sensor_code, sensor.user_id])
        return sensor
    
    def get(self, sensor_code):
        with open('./repository/sensor.csv', "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) > 0 and row[2] == sensor_code:
                    return row
        return []