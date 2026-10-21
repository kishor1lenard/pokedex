import sqlite3

# Nom du fichier de la base
DATABASE = "pokedex.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    
    # permet de lire les colonnes par leur nom : row["name"] au lieu de row[1]
    connection.row_factory = sqlite3.Row
    return connection