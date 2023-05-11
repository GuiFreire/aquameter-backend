from repository.user_repository import UserRepository
from models.user import User

class UserController:
    def create(self, name, document, password):
        user = User(id=id, name=name, document=document, password=password)
        
        response = UserRepository().create(user)
        
        return {"name": response.name, "document": response.document, "password": response.password}
    
    def get(self,  id):
        response = UserRepository().get(id)
        
        if len(response) > 0:
            return response
        else:
            return {}