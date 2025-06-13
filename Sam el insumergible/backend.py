from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route("/nombre")
def nombre():
    descripcion_html = """
    <h1 mt-4 >Sam el Insumergible</h1>
    """
    return descripcion_html 

@app.route("/inicio")
def inicio():
    descripcion_html = """
    <h1 class="lead">¡El gato que sobrevivió 3 naufragios!</h1>
    <img 
        class="img-fluid barcos" 
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFjBBYZc_B9H6VwUTHHaHjgXPGG6yunBbbdw&s" 

    />
    """
    return descripcion_html


@app.route("/descripcion")
def descripcion():
    descripcion_html = """
    <h2 class="bg-cafe2 text-dark text-center">¿Quién es Sam?</h2>
    <p>
        Unsinkable Sam, originalmente conocido como Oscar, fue un gato que se convirtió en una leyenda de la Segunda Guerra Mundial al sobrevivir al hundimiento de tres buques de guerra.
        Su historia comienza a bordo del acorazado alemán Bismarck, pasa por el destructor británico HMS Cossack y termina en el portaaviones HMS Ark Royal, escapando cada vez de las aguas del Atlántico con vida.
    </p>
    """
    return descripcion_html 

