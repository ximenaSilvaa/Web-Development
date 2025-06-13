import sqlite3

try:
    with sqlite3.connect("cafeBigotesDataBase.db") as conn:
        cur = conn.cursor()
        
        # Crear las tablas si no existen
        cur.execute("""CREATE TABLE IF NOT EXISTS Platillos(
                    id INTEGER PRIMARY KEY,
                    Nombre TEXT, 
                    Precio FLOAT, 
                    Info TEXT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Gatos(
                    id INTEGER PRIMARY KEY, 
                    Nombre TEXT, 
                    Foto TEXT, 
                    Info TEXT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Usuarios(
                    id INTEGER PRIMARY KEY, 
                    Usuario TEXT, 
                    Contraseña TEXT)""")
        
        # Insertar platillos
        platillos = [
            ("Café Americano", 40, "Café negro con granos seleccionados."),
            ("Café Latte", 50, "Café con leche espumosa."),
            ("Sándwich de pollo", 85, "Pan artesanal con pollo y aguacate."),
            ("Pastel de zanahoria", 55, "Pastel con nueces y crema de queso."),
            ("Matcha Latte", 60, "Bebida de té matcha con leche espumosa."),
            ("Chai Latte", 55, "Té negro con especias y leche vaporizada."),
            ("Croissant de almendra", 45, "Hojaldre relleno con crema de almendra."),
            ("Tostadas de aguacate", 70, "Pan artesanal con aguacate, tomate cherry y semillas."),
            ("Galletas de chispas de chocolate", 35, "Galletas caseras con chispas de chocolate."),
            ("Cheesecake de frutos rojos", 65, "Cheesecake cremoso con cobertura de frutos rojos."),
        ]
        cur.executemany("INSERT INTO Platillos (Nombre, Precio, Info) VALUES (?, ?, ?)", platillos)

        # Insertar gatos
        gatos = [
            ("Luis", "https://blog.felinus.cl/wp-content/uploads/2023/03/gato-esfinge-5.png", "Gato esfinge."),
            ("Carlos","https://miauu.mx/wp-content/uploads/2022/03/Gato-persa-azul.jpg", "Gato persa."),
            ("José", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmzb1T-wHLJovrfzfCMSzMz2ereJI-8h2fKw&s", "Gato siberiano."),
            ("Mariano", "https://mascooriente.co/wp-content/uploads/2021/08/ruzo-azul.jpeg", "Gato ruso azul."),
            ("Emiliasno", "https://www.elespectador.com/resizer/v2/KHYLDDXDT5BCLBABKRR6LXRLQU.jpg?auth=4c5e75f2a4c4bbfea212303df378c1aa93ef2b6ca88d27192f397b890475a201&width=1200&height=675&smart=true&quality=80", "Gato British Shorthair.")
        ]
         
        cur.executemany("INSERT INTO Gatos (Nombre, Foto, Info) VALUES (?, ?, ?)", gatos)

        print("Base de datos creada exitosamente.")

except sqlite3.OperationalError as e:
    print("Error al crear la base de datos:", e)
