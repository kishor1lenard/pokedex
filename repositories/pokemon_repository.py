import json

from db.database import get_connection
from schemas.pokemon import Pokemon


# Transforme une ligne de la table pokemon en objet Pokemon
def row_to_pokemon(row):
    return Pokemon(
        number=row["number"],
        name=row["name"],
        name_fr=row["name_fr"],
        types=json.loads(row["types"]),  # le texte JSON redevient une liste
        image_url=row["image_url"],
        height=row["height"],
        weight=row["weight"],
        evolves_from_number=row["evolves_from_number"],
    )


# Renvoie le Pokémon s'il est dans la base, sinon None
def get_pokemon_by_number(number: int):
    connection = get_connection()
    cursor = connection.cursor()
    # le ? évite les injections SQL (et (number,) avec une virgule = tuple)
    cursor.execute("SELECT * FROM pokemon WHERE number = ?", (number,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None
    return row_to_pokemon(row)


# Enregistre un Pokémon dans la base
def insert_pokemon(pokemon: Pokemon):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO pokemon (number, name, name_fr, types, image_url, height, weight, evolves_from_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon.number,
            pokemon.name,
            pokemon.name_fr,
            # SQLite n'a pas de type liste -> on stocke la liste en texte JSON
            json.dumps(pokemon.types, ensure_ascii=False),
            pokemon.image_url,
            pokemon.height,
            pokemon.weight,
            pokemon.evolves_from_number,
        ),
    )
    connection.commit()
    connection.close()