from flask import Flask ,jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/verificar", methods = ["POST"])
def verificar():
    usuario = request.form["usuario"]
    contraseña = request.form["contraseña"]
    if usuario == "Admin" and contraseña == "1234":
        resultado = "Login correcto"
        return resultado
    else:
        return "Login incorrecto"
