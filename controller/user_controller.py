from repository.user_repository import UserRepository
from models.user import User

class UserController:
    def create(self, name, document, password):
        user = User(id=id, name=name, document=document, password=password)
        
        response = UserRepository().create(user)
        
        return "Success to create User"
    
    def get(self,  id):
        response = UserRepository().get(id)
        
        if len(response) > 0:
            return { "id": response[0], "name": response[1], "document": response[2] }
        else:
            return {}