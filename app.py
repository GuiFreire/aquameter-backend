from flask import Flask, request
from controller.user_controller import UserController
from controller.sensor_controller import SensorController
from controller.record_controller import RecordController
from controller.phone_controller import PhoneController

app = Flask(__name__)

@app.route("/user", methods = ["POST", "GET"])
def user():
    if request.method == "POST":
        data = request.get_json() # pega o body da requisiçao
        name = data["name"]
        document = data["document"]
        password = data["password"]

        return UserController().create(name, document, password)
    elif request.method == "GET":
        _id = request.args.get("id")

        return UserController().get(_id)


@app.route("/sensor", methods = ["POST", "GET"])
def sensor():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        sensor_code = data["sensor_code"]
        user_id = data["user_id"]

        return SensorController().create(name, sensor_code, user_id)
    elif request.method == "GET":
        sensor_code = request.args.get("sensor_code")

        return SensorController().get(sensor_code)
    

@app.route("/record", methods = ["POST", "GET"])
def record():
    if request.method == "POST":
        data = request.get_json()
        sensor_code = data["sensor_code"]
        volume = data["volume"]

        return RecordController().create(sensor_code, volume)
    elif request.method == "GET":
        sensor_code = request.args.get("sensor_code")

        return RecordController().get(sensor_code)
    
@app.route("/phone", methods = ["POST", "GET"])
def phone():
    if request.method == "POST":
        data = request.get_json()
        phone_number = data["phone_number"]
        user_id = data["user_id"]

        return PhoneController().create(phone_number, user_id)
    elif request.method == "GET":
        user_id = request.args.get("user_id")

        return PhoneController().get(user_id)