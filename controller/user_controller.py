from repository.user_repository import UserRepository
from models.user import User

class UserController:
    def create(self, name, document, password):
        user = User(id=id, name=name, document=document, password=password)
        
        response = UserRepository().create(user)
        
        return {"name": response.name, "document": response.document, "password": response.password}
    

    def get(self, document, password):
        response = UserRepository().get(document, password)

        if len(response) > 0: 
            user = response[0]
            return {"id": user[0], "name": user[1], "document": user[2], "password": user[3]}
        else:
            return "Nenhum usuário encontrado"