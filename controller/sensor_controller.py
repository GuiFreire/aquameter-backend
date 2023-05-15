from repository.sensor_repository import SensorRepository
from models.sensor import Sensor
from repository.user_repository import UserRepository

class SensorController:
    def create(self, name, sensor_code, user_id):
        sensor = Sensor(name=name, sensor_code=sensor_code, user_id=user_id)

        user = UserRepository().get(user_id)
        
        if len(user) > 0 :
            response = SensorRepository().create(sensor)
        
            return {"name": response.name, "sensor_code": response.sensor_code, "user_id": response.user_id }
        else:
            return "Usuário inválido"

    def get(self,  sensor_code):
        response = SensorRepository().get(sensor_code)
        
        if len(response) > 0:
            return response
        else:
            return {}