from src.api_client import get_pokemon_info
from src.utills import display_pokemon
import requests

pokemon_name = input("Enter Pokemon name: ").strip().lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    display_pokemon(pokemon_info)