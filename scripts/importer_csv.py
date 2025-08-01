import pandas as pd
import sqlite3
from pathlib import Path

# Charger le CSV
df = pd.read_csv("data/ventes.csv")

# Connexion SQLite
conn = sqlite3.connect("db/ventes.db")
df.to_sql("ventes", conn, if_exists="replace", index=False)

print("Import terminé avec succès.")