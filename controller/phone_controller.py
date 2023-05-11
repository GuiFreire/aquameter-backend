from repository.phone_repository import PhoneRepository
from models.phone import Phone

class PhoneController:
    def create(self, phone_number, user_id):
        phone = Phone(id=id, phone_number=phone_number, user_id=user_id)
        
        response = PhoneRepository().create(phone)
        
        return {"phone_number": response.phone_number, "user_id": response.user_id}
    
    def get(self,  user_id):
        response = PhoneRepository().get(user_id)
        
        if len(response) > 0:
            return response
        else:
            return "Nenhum registro encontrado"