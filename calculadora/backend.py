from flask import Flask ,jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/suma", methods = ["POST"])
def suma():
    fNumber = int(request.form["first"])
    sNumber = int(request.form["second"])
    resultado = fNumber + sNumber
    return str(resultado)

@app.route("/resta", methods = ["POST"])
def resta():
    fNumber = int(request.form["first"])
    sNumber = int(request.form["second"])
    resultado = fNumber - sNumber
    return str(resultado)

@app.route("/multiplicacion", methods = ["POST"])
def multiplicacion():
    fNumber = int(request.form["first"])
    sNumber = int(request.form["second"])
    resultado = fNumber * sNumber
    return str(resultado)

@app.route("/division", methods = ["POST"])
def division():
    fNumber = int(request.form["first"])
    sNumber = int(request.form["second"])
    resultado = fNumber / sNumber
    return str(resultado)
