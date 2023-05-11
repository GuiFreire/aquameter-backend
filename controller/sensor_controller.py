from repository.sensor_repository import SensorRepository
from models.sensor import Sensor

class SensorController:
    def create(self, name, sensor_code, user_id):
        sensor = Sensor(name=name, sensor_code=sensor_code, user_id=user_id)
        
        response = SensorRepository().create(sensor)
        
        return {"name": response.name, "sensor_code": sensor_code, "user_id": response.user_id }
    
    def get(self,  document):
        response = SensorRepository().get(document)
        
        if len(response) > 0:
            return {"name": response[0], "sensor_code": response[1], "user_id": response[2] }
        else:
            return {}