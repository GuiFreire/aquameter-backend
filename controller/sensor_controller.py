from repository.sensor_repository import SensorRepository
from models.sensor import Sensor
from repository.user_repository import UserRepository
from repository.relationship_repository import RelationshipRepository

class SensorController:
    def create(self, name, sensor_code, user_id):
        sensor = Sensor(name=name, sensor_code=sensor_code, user_id=user_id)

        user = UserRepository().getByUserId(user_id)
        
        if len(user) > 0 :
            response = SensorRepository().create(sensor)
        
            return {"name": response.name, "sensor_code": response.sensor_code, "user_id": response.user_id }
        else:
            return "Usuário inválido"

    def get(self,  user_id):
        relationship = RelationshipRepository().get(user_id)

        if len(relationship) > 0:
            response = SensorRepository().getByRelationship(user_id)
        else:
            response = SensorRepository().get(user_id)
        
        data = []
        if len(response) > 0:
            for i in response:
                data.append({"sensor_code": i[0], "name": i[1], "user_id": i[2]})
            return data
        else:
            return "Nenhum sensor encontrado"