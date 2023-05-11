from repository.relationship_repository import RelationshipRepository
from models.relationship import RelationShip

class RelationshipController:
    def create(self, user_id, parent_user_id, user_sensor_code):
        relationship = RelationShip(id=id, user_id=user_id, parent_user_id=parent_user_id, user_sensor_code=user_sensor_code)
        
        response = RelationshipRepository().create(relationship)
        
        return {"user_id": response.user_id, "parent_user_id": response.parent_user_id, "user_sensor_code": response.user_sensor_code }
    
    def get(self,  parent_user_id):
        response = RelationshipRepository().get(parent_user_id)
        
        if len(response) > 0:
            return response
        else:
            return {}