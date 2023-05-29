from repository.phone_repository import PhoneRepository
from models.phone import Phone
from repository.user_repository import UserRepository

class PhoneController:
    def create(self, phone_number, user_id):
        phone = Phone(id=id, phone_number=phone_number, user_id=user_id)

        user = UserRepository().get(user_id)

        if len(user) > 0 :
            response = PhoneRepository().create(phone)
            return {"phone_number": response.phone_number, "user_id": response.user_id}
        else :
            return "Usuário não existe"
    
    def get(self,  user_id):
        response = PhoneRepository().get(user_id)
        
        phones = []
        if len(response) > 0:
            for i in response:
                phones.append(i[1])

            return {"phones": phones}
        else:
            return "Nenhum registro encontrado"