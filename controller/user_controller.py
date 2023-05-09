from repository.user_repository import UserRepository
from models.user import User

class UserController:
    def create(self,  id, name, document, password):
        user = User(id=id, name=name, document=document, password=password)
        
        response = UserRepository().create(user)
        
        return { "id": response.id, "name": response.name, "document": response.document }
    
    def get(self,  document):
        response = UserRepository().get(document)
        
        if len(response) > 0:
            return { "id": response[0], "name": response[1], "document": response[2] }
        else:
            return {}