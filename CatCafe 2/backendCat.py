from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3
import hashlib

app = Flask(__name__)
CORS(app) 

@app.route("/nombreCafe")
def nombre_cafe():
    descripcion_html = """
    <h1>Café Bigotes</h1>
    """
    return descripcion_html 

@app.route("/animacion")
def animacion():
    descripcion_html = """
    <h1 class="lead">¡Toca al gato para que se mueva!</h1>
    <img 
        class="gato" 
        src="https://www.shutterstock.com/shutterstock/videos/4094146/thumb/6.jpg?ip=x480" 
        alt="Gato que se mueve"
    />
    """
    return descripcion_html


@app.route("/descripcion")
def descripcion():
    descripcion_html = """
    <h2 class="bg-cafe2 text-white text-center">Descripción</h2>
    <p>
          Bienvenidos a Cat Cafe, un refugio donde el café se mezcla con la magia de los gatos. 
          Disfruta de una deliciosa taza de café, té o un antojito mientras te relajas en la compañía 
          de adorables gatos. Nuestro espacio está diseñado para brindarte un ambiente tranquilo y acogedor, 
          ideal para disfrutar de un momento de calma o pasar un rato agradable con amigos.
    </p>
    """
    return descripcion_html 

@app.route("/menu")
def menu():
    try:
        with sqlite3.connect("cafeBigotesDataBase.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT Nombre, Precio FROM Platillos")
            menu_items = cur.fetchall()

        html_menu = "<ul>" + "".join(f"<li>{nombre} - ${precio}</li>" for nombre, precio in menu_items) + "</ul>"
        return html_menu

    except sqlite3.Error as e:
        return f"Error al obtener el menú: {e}"
    
@app.route("/logo")
def logo():
    descripcion_html = """
    <img
          class="img-fluid rounded"
          src="data:image/jpeg;base64,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"
          alt="logo"
          width="420" 
    />
    """
    return descripcion_html 

@app.route("/tituloGatos")
def tituloGatos():
    descripcion_html = """
     <h2 class= "bg-cafe2 text-white text-center">Estos son nuestros gatitos</h2>
    """
    return descripcion_html 

@app.route("/infoGatos")
def obtener_gatos():
    try:
        with sqlite3.connect("cafeBigotesDataBase.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT Nombre, Foto, Info FROM Gatos LIMIT 3")  
            gatos = cur.fetchall()  

        if not gatos:
            return "<p>No hay gatos en la base de datos.</p>"

        html_gatos = ""  

        for i, (nombre, foto, info) in enumerate(gatos, start=1):
            html_gatos += f"""
            <div class="row border p-5">
                <div class="col-sm-4 text-center">
                    <h4 class="bg-cafe2 text-white text-center py-2 rounded mb-3">{nombre}</h4>
                    <img id="gato{i}" class="img-fluid rounded mb-3" width="420" src="{foto}" alt="Gatito {nombre}" />
                    <button type="button" class="btn btn-dark bg-cafe" id="btnGato{i}">Información de {nombre}</button>
                    <figcaption id="infoGato{i}" class="mt-3" style="display: none;">
                        {info}
                    </figcaption>
                </div>
            </div>
            """

        return html_gatos  

    except sqlite3.Error as e:
        return f"<p>Error al obtener los gatos: {e}</p>", 500

@app.route("/horarios")
def horarios():
    descripcion_html= """
        <h2 class= "bg-cafe2 text-white text-center">Horarios</h2>
        <p>
          Abierto de Lunes a Viernes de 9:00 a.m. a 14:00 p.m.
        </p>
    """
    return descripcion_html


@app.route("/ubicacion")
def ubicacion():
    descripcion_html= """
        <h2 class= "bg-cafe2 text-white text-center">Ubicación</h2>
        <i>
          Ubicado en el corazón de la ciudad, en la calle Puesta del Sol número 14, 
          justo a unos pasos del Parque Felinos.
        </i>
    """
    return descripcion_html

@app.route("/mapa")
def mapa():
    descripcion_html= """
        <h2 class= "bg-cafe2 text-white text-center">Mapa</h2>
        <img 
          class="img-fluid rounded"
          src="https://i.blogs.es/7a5f56/mapas-tiempo-real/450_1000.jpg"
          alt="Mapa de ubicación"
        />
    """
    return descripcion_html



@app.route('/foto')
def cambiar_fotos():
    return [
        "https://www.hospitalveterinariouax.com/var/site/storage/images/1/3/2/3/73231-1-esl-ES/hero-gato-egypcio-blog.jpg",
        "https://www.racoesreis.com.br/wordpress/wp-content/uploads/gato-origem2.jpg",
        "https://cattime.com/wp-content/uploads/sites/14/2011/12/GettyImages-1361394182-e1699287824483.jpg?w=1024"
    ],200



@app.route("/signup", methods=["POST"])
def signup():
    usuarioUsuarios = request.form["usuario"]
    contraseñaUsuarios = request.form["contraseña"]
    contraseña_hash = encriptar_contraseña(contraseñaUsuarios)  

    try:
        with sqlite3.connect("cafeBigotesDataBase.db") as conn:
            cur = conn.cursor()

            cur.execute("INSERT INTO Usuarios(Usuario, Contraseña) VALUES (?,?)",
                        (usuarioUsuarios, contraseña_hash))  
            conn.commit()
            return jsonify({"success": True, "message": "Usuario registrado exitosamente"})

    except sqlite3.OperationalError as e:
        return jsonify({"success": False, "message": "Error en la base de datos: " + str(e)})

# Función para encriptar contraseñas antes de compararlas
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para validar usuario en la base de datos
def validar_usuario(usuario, contraseña):
    try:
        with sqlite3.connect("cafeBigotesDataBase.db") as conn:
            cur = conn.cursor()

            contraseña_hash = encriptar_contraseña(contraseña)  # Encriptar la contraseña ingresada
            
            # Buscar el usuario con la contraseña encriptada
            cur.execute("SELECT * FROM Usuarios WHERE Usuario = ? AND Contraseña = ?", (usuario, contraseña_hash))
            resultado = cur.fetchone()

            if resultado:
                return True  # Usuario válido
            else:
                return False  # Usuario incorrecto

    except sqlite3.Error as e:
        print("Error al acceder a la base de datos:", e)
        return False

# Ruta para verificar login
@app.route("/verificar", methods=["POST"])
def verificar():
    datos = request.json  # Recibir datos en formato JSON desde el frontend
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if validar_usuario(usuario, contraseña):
        return jsonify({"success": True, "message": "Inicio de sesión exitoso"})
    else:
        return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"})

if __name__ == "__main__":
    app.run(debug=True)  # Ejecutar el servidor Flask
