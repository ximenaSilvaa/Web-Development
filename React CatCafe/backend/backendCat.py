from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def get_db_connection():
    conn = sqlite3.connect("cafeBigotesDataBase.db")
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para el nombre
@app.route("/nombreCafe")
def nombre_cafe():
    return jsonify({"nombre": "Café Bigotes"})

# Ruta para la animación
@app.route("/animacion")
def animacion():
    return jsonify({
        "imagen": "https://www.shutterstock.com/shutterstock/videos/4094146/thumb/6.jpg?ip=x480"
    })

@app.route("/textoAnimacion")
def texto_animacion():
    return jsonify({"animacion": "¡Toca al gato para que se mueva!"})

# Ruta para la descripción
@app.route("/descripcion")
def descripcion():
    return jsonify({
        "titulo": "Descripción",
        "contenido": """Bienvenidos a Cat Cafe, un refugio donde el café se mezcla con la magia de los gatos. 
          Disfruta de una deliciosa taza de café, té o un antojito mientras te relajas en la compañía 
          de adorables gatos. Nuestro espacio está diseñado para brindarte un ambiente tranquilo y acogedor, 
          ideal para disfrutar de un momento de calma o pasar un rato agradable con amigos."""
    })

# Ruta para el menu
@app.route("/menu")
def menu():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT Nombre, Precio, Info FROM Platillos")
        platillos = [{"nombre": row["Nombre"], "precio": row["Precio"], "info": row["Info"]} for row in cur.fetchall()]
        conn.close()
        return jsonify({"menu": platillos})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

# Ruta para el logo 
@app.route("/logo")
def logo():
    return jsonify({
        "titulo": "Menu",
        "imagen": "data:image/jpeg;base64,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"
    })

# Ruta para el logo 
@app.route("/tituloGatos")
def tituloGatos():
    return jsonify({
        "titulo": "Nuestros Gatitos"
    })


# Ruta para obtener los gatos desde la base de datos
@app.route("/infoGatos")
def obtener_gatos():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT Nombre, Foto, Info FROM Gatos LIMIT 5")
        gatos = [{"nombre": row["Nombre"], "foto": row["Foto"], "info": row["Info"]} for row in cur.fetchall()]
        conn.close()
        return jsonify({"gatos": gatos})
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

# Ruta para los horarios
@app.route("/horarios")
def horarios():
    return jsonify({
        "titulo": "Horarios de Atención", 
        "horarios": [
            {"dia": "Lunes - Viernes", "horario": "8:00 AM - 10:00 PM"},
            {"dia": "Sábado - Domingo", "horario": "9:00 AM - 11:00 PM"}
        ]
    })

# Ruta para la ubicación
@app.route("/ubicacion")
def ubicacion():
    return jsonify({
        "titulo": "Ubicación",
        "ubicacion": "Calle Puesta del Sol #14, cerca del Parque Felinos",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.781221743282!2d-74.06492752501195!3d4.647964795698406!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f9b7e01e42f3d%3A0x1c348fd1734902fd!2sParque%20de%20Los%20Gatos!5e0!3m2!1ses!2sco!4v1709823945872!5m2!1ses!2sco"
    })


# Ruta para la descripción
@app.route("/footer")
def footer():
    return jsonify({
        "copyright": "© 2025 Café Bigotes",
        "slogan": "Un café con amor y bigotes"
    })

def get_db_connection():
    conn = sqlite3.connect("cafeBigotesDataBase.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/iniciarSesion/texto', methods=['GET'])
def inicio_textos():
    return jsonify({
        "titulo": "Iniciar Sesión",
        "texto_boton": "Acceder"
    })

# Ruta para iniciar sesión
@app.route("/iniciarSesion", methods=["POST"])
def iniciar_sesion():
    try:
        data = request.get_json()
        usuario = data.get("usuario")
        contraseña = data.get("contraseña")

        if not usuario or not contraseña:
            return jsonify({"message": "Usuario y contraseña son obligatorios"}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Usuarios WHERE Usuario = ? AND Contraseña = ?", (usuario, contraseña))
        usuario_encontrado = cur.fetchone()
        conn.close()

        if usuario_encontrado:
            return jsonify({"message": "Inicio de sesión exitoso"}), 200
        else:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

    except Exception as e:
        return jsonify({"message": f"Error al iniciar sesión: {str(e)}"}), 500

# Ruta para el texto
@app.route('/registrar/texto', methods=['GET'])
def registrar_textos():
    return jsonify({
        "titulo": "Registro de Usuario",
        "texto_boton": "Registrarse"
    })

# Ruta para registrar un usuario
@app.route("/registrar", methods=["POST"])
def registrar_usuario():
    try:
        data = request.get_json()
        usuario = data["usuario"]
        contraseña = data["contraseña"]

        if not usuario or not contraseña:
            return jsonify({"message": "Usuario y contraseña son obligatorios"}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("INSERT INTO Usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
        conn.commit()
        conn.close()

        return jsonify({"message": "Usuario registrado con éxito"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"message": "El usuario ya existe"}), 409

    except Exception as e:
        return jsonify({"message": f"Error al registrar usuario: {str(e)}"}), 500


# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)
