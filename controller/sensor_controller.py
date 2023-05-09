from repository.sensor_repository import SensorRepository
from models.sensor import Sensor

class SensorController:
    def create(self,  id, name, sensor_code, user_id):
        sensor = Sensor(id=id, name=name, sensor_code=sensor_code, user_id=user_id)
        
        response = SensorRepository().create(sensor)
        
        return { "id": response.id, "name": response.name, "sensor_code": sensor_code, "user_id": response.user_id }
    
    def get(self,  document):
        response = SensorRepository().get(document)
        
        if len(response) > 0:
            return { "id": response[0], "name": response[1], "sensor_code": response[2], "user_id": response[3] }
        else:
            return {}