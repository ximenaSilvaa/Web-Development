import sqlite3


try:
    with sqlite3.connect("animeDataBase.db") as conn:

        cur = conn.cursor()
        # Tabla de creadores
        cur.execute("""CREATE TABLE Creadores(id INTEGER PRIMARY KEY,
                    Nombre TEXT, Edad INTEGER, Info TEXT)""")

        # Tabla de animes
        cur.execute("""CREATE TABLE Animes(id INTEGER PRIMARY KEY, 
                    Nombre TEXT,Creador INTEGER, Genero TEXT,
                    FOREIGN KEY(Creador) REFERENCES Creadores(id))""")
        
        pass

except sqlite3.OperationalError as e:
    print("Failed to open database:", e)
