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
            return "Nenhum sensor encontrado"
        
    
    def get(self,  sensor_code):
        response = RecordRepository().get(sensor_code)
        
        data = []
        if len(response) > 0:
            for i in response:
                data.append({"Sensor_Code": i[0], "Volume": i[1], "Date": i[2]})
            return response
        else:
            return "Nenhum registro encontrado"
        
    
    def getByMonth(self, sensor_code):
        response = RecordRepository().getByMonth(sensor_code)

        data = []
        if len(response) > 0:
            for i in response:
                data.append({"volume": i[0], "month": i[1]})
            return data
        else:
            return "Nenhum registro encontrado"
        
    
    def getByDay(self, sensor_code):
        response = RecordRepository().getByDay(sensor_code)

        data = []
        if len(response) > 0:
            for i in response:
                data.append({"volume": i[0], "day": i[1]})
            return data
        else:
            return "Nenhum registro encontrado"