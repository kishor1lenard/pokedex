import requests
from fastapi import FastAPI, HTTPException
from clients.pokeapi import get_pokemon_from_api
from schemas.pokemon import Pokemon
from repositories.pokemon_repository import get_pokemon_by_number, insert_pokemon

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# Version 1 : on interroge PokéAPI directement à chaque consultation
@app.get("/pokemons/{number}")
def get_pokemon(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url, timeout=10)

    # Numéro inconnu (ou autre problème) -> 404
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    data = response.json()
    # On ne garde que les champs utiles
    return {
        "number": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],  
    }



# Scan : récupère UN Pokémon sur PokéAPI et l'enregistre dans SQLite
@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan(number: int):
    data = get_pokemon_from_api(number)
    if data is None:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    pokemon = Pokemon(
        number=data["id"],
        name=data["name"],
        name_fr=data["name"],
        types=[entry["type"]["name"] for entry in data["types"]],
        image_url=data["sprites"]["front_default"],
        height=data["height"],
        weight=data["weight"],
        evolves_from_number=None,
    )
    insert_pokemon(pokemon)
    return pokemon