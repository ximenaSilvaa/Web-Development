from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)


@app.route("/increador", methods=["POST"])
def increador():
    idCreador = request.form["identifier"]
    nombreCreador = request.form["name"]
    edadCreador = request.form["age"]
    infoCreador = request.form["info"]

    try:
        with sqlite3.connect("animeDataBase.db") as conn:

            cur = conn.cursor()

            cur.execute("INSERT INTO Creadores(id,Nombre,Edad,Info) VALUES (?,?,?,?)",
                        (idCreador, nombreCreador, edadCreador, infoCreador))
            conn.commit()

            consulta = cur.execute("SELECT * FROM Creadores;")
            resultado = consulta.fetchone()
            print(resultado)
            pass

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)

    return "saved data"
