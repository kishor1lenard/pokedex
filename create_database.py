import sqlite3

connection = sqlite3.connect("pokedex.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        number INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        name_fr TEXT NOT NULL,
        types TEXT NOT NULL,
        image_url TEXT NOT NULL,
        height INTEGER NOT NULL,
        weight INTEGER NOT NULL,
        evolves_from_number INTEGER
    )
""")

connection.commit()
connection.close()

print("Base de données créée avec succès.")