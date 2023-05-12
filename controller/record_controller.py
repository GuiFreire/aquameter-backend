from repository.record_repository import RecordRepository
from repository.sensor_repository import SensorRepository
from models.record import Record
import datetime

class RecordController:
    def create(self, sensor_code, volume):
        record = Record(id=id, sensor_code=sensor_code, volume=volume, date=datetime.datetime.now())

        sensor = SensorRepository().get(sensor_code)

        if len(sensor) > 0:
            response = RecordRepository().create(record)
            return {"sensor_code": response.sensor_code, "volume": response.volume, "date": response.date }
        else:
            return {"Nenhum sensor encontrado"}
        
    
    def get(self,  sensor_code):
        response = RecordRepository().get(sensor_code)
        
        if len(response) > 0:
            return response
        else:
            return "Nenhum registro encontrado"