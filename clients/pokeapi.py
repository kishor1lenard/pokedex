import requests

BASE_URL = "https://pokeapi.co/api/v2"


# Récupère les infos d'un Pokémon sur PokéAPI
def get_pokemon_from_api(number: int):
    url = f"{BASE_URL}/pokemon/{number}"
    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        return None
    response.raise_for_status()

    return response.json()