import sqlite3
import pandas as pd

conn = sqlite3.connect("db/ventes.db")

# Analyse simple
df = pd.read_sql("SELECT magasin, SUM(ca) AS total_ca FROM ventes GROUP BY magasin", conn)
print(df)

conn.close()