from repository.record_repository import RecordRepository
from models.record import Record
import datetime

class RecordController:
    def create(self, sensor_code, volume):
        sensor = Record(id=id, sensor_code=sensor_code, volume=volume, date=datetime.datetime.now())
        
        response = RecordRepository().create(sensor)
        
        return {"sensor_code": response.sensor_code, "volume": response.volume, "date": response.date }
    
    def get(self,  sensor_code):
        response = RecordRepository().get(sensor_code)
        
        if len(response) > 0:
            return response
        else:
            return "Nenhum registro encontrado"