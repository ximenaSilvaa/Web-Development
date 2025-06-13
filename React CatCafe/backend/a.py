import sqlite3
import pandas as pd
try:
    with sqlite3.connect("cafeBigotesDataBase.db") as conn:
        cur = conn.cursor()
        consulta = cur.execute("SELECT * FROM Gatos")
        print(consulta.fetchall())
        df = pd.read_sql_query("SELECT * FROM Gatos", conn)
        df = df.sort_values(by = "Nombre", ascending = False)
        print(df.head())
        df.to_excel("excel1.xlsx")
    pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)