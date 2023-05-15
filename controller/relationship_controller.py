from repository.relationship_repository import RelationshipRepository
from models.relationship import RelationShip
from repository.user_repository import UserRepository
from repository.sensor_repository import SensorRepository

class RelationshipController:
    def create(self, user_id, parent_user_id, user_sensor_code):
        relationship = RelationShip(id=id, user_id=user_id, parent_user_id=parent_user_id, user_sensor_code=user_sensor_code)

        sensor = SensorRepository.get(user_sensor_code)

        user = UserRepository.get(parent_user_id)

        if (len(sensor) > 0) and (len(user) > 0) :
            response = RelationshipRepository().create(relationship)
            
            return {"user_id": response.user_id, "parent_user_id": response.parent_user_id, "user_sensor_code": response.user_sensor_code }
        else:
            return "Sensor ou usuário inválido"
    
    def get(self,  parent_user_id):
        response = RelationshipRepository().get(parent_user_id)
        
        if len(response) > 0:
            return response
        else:
            return {}