import sqlite3

try:
    with sqlite3.connect("cafeBigotesDataBase.db") as conn:

        cur = conn.cursor()
        
        # Tabla de platillos
        cur.execute("""CREATE TABLE IF NOT EXISTS Platillos(
                    id INTEGER PRIMARY KEY,
                    Nombre TEXT, 
                    Precio FLOAT, 
                    Info TEXT)""")

        # Tabla de gatos
        cur.execute("""CREATE TABLE IF NOT EXISTS Gatos(
                    id INTEGER PRIMARY KEY, 
                    Nombre TEXT, 
                    Foto TEXT, 
                    Info TEXT)""")

        # Tabla de usuarios
        cur.execute("""CREATE TABLE IF NOT EXISTS Usuarios(
                    id INTEGER PRIMARY KEY, 
                    Usuario TEXT, 
                    Contraseña TEXT)""")
        
        # Insertar platillos
        platillos = [
            ("Café Americano", 40, "Café negro con granos seleccionados."),
            ("Café Latte", 50, "Café con leche espumosa."),
            ("Sándwich de pollo con aguacate", 85, "Pan artesanal, pollo desmenuzado y aguacate fresco."),
            ("Pastel de zanahoria", 55, "Pastel esponjoso con nueces y crema de queso."),
            ("Focaccia de romero y aceitunas", 50, "Pan italiano con aceite de oliva, romero y aceitunas.")
        ]

        cur.executemany("INSERT INTO Platillos (Nombre, Precio, Info) VALUES (?, ?, ?)", platillos)

        # Insertar gatos
        gatos = [
            ("Ana", "https://blog.felinus.cl/wp-content/uploads/2023/03/gato-esfinge-5.png", "Esta gatita es un gato esfinge."),
            ("María", "https://miauu.mx/wp-content/uploads/2022/03/Gato-persa-azul.jpg", "Esta gatita es un gato siamés al que le gusta ser acariciado."),
            ("Sofía", "https://www.elespectador.com/resizer/v2/KHYLDDXDT5BCLBABKRR6LXRLQU.jpg?auth=4c5e75f2a4c4bbfea212303df378c1aa93ef2b6ca88d27192f397b890475a201&width=1200&height=675&smart=true&quality=80", "Esta gatita es un British Shorthair muy amigable.")
        ]

        cur.executemany("INSERT INTO Gatos (Nombre, Foto, Info) VALUES (?, ?, ?)", gatos)

        print("Datos insertados correctamente.")

except sqlite3.OperationalError as e:
    print("Failed to open database:", e)
