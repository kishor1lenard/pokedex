import requests
from fastapi import FastAPI, HTTPException
from schemas.pokemon import Pokemon

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

