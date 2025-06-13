import sqlite3

try:
    with sqlite3.connect("cafeBigotesDataBase.db") as conn:
        cur = conn.cursor()
       
        gatos = [
            ("Omar", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIa9fccdICT-crU7vTc1t7uj0XudqBlqpGfw&s", "Gato Oriental")
        ]
         
        cur.executemany("INSERT INTO Gatos (Nombre, Foto, Info) VALUES (?, ?, ?)", gatos)

        print("insertado")

except sqlite3.OperationalError as e:
    print("Error al crear la base de datos:", e)
