import sqlite3
import hashlib

def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

def validar_usuario(usuario, contraseña):
    try:
        with sqlite3.connect("cafeBigotesDataBase.db") as conn:
            cur = conn.cursor()

            contraseña_hash = encriptar_contraseña(contraseña)  # Encriptar la ingresada
            cur.execute("SELECT * FROM Usuarios WHERE Usuario = ? AND Contraseña = ?", (usuario, contraseña_hash))
            
            resultado = cur.fetchone()  # Obtener el primer resultado

            if resultado:
                print("Inicio de sesión exitoso. ¡Bienvenido!")
                return True
            else:
                print("Usuario o contraseña incorrectos.")
                return False

    except sqlite3.Error as e:
        print("Error al acceder a la base de datos:", e)
        return False
