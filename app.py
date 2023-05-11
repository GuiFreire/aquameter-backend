from flask import Flask, request
from controller.user_controller import UserController
from controller.sensor_controller import SensorController

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
        document = request.args.get("document")

        return UserController().get(document)


@app.route("/sensor", methods = ["POST", "GET"])
def sensor():
    if request.method == "POST":
        data = request.get_json()
        _id = data["id"]
        name = data["name"]
        sensor_code = data["sensor_code"]
        user_id = data["user_id"]

        return SensorController().create(_id, name, sensor_code, user_id)
    elif request.method == "GET":
        sensor_code = request.args.get("sensor_code")

        return SensorController().get(sensor_code)