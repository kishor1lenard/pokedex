from typing import List, Optional
from pydantic import BaseModel

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