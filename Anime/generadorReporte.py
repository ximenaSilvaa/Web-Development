import sqlite3
import pandas as pd
try:
    with sqlite3.connect("441semana4/animeDataBase.db") as conn:
        cur = conn.cursor()
        consulta = cur.execute("SELECT * FROM Creadores")
        print(consulta.fetchall())
        df = pd.read_sql_query("SELECT * FROM Creadores", conn)
        print(df.head())
        df.to_excel("excel1.xlsx")
    pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)