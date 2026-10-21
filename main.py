import requests
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Fiche Pokémon renvoyée par l'API
class Pokemon(BaseModel):
    number: int                                
    name: str                                  
    name_fr: str                               
    types: List[str]                       
    image_url: str                            
    height: int                                 # en centimètres
    weight: int                                 # en grammes
    evolves_from_number: Optional[int] = None   # None si pas de pré-évolution en Gen 1


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

