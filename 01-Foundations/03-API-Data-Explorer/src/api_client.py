import requests 
from .models import Pokemon

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.Timeout:
            print(f"Attempt: {attempt + 1}: Request Timed out.")
        except requests.exceptions.RequestException:
            print(f"Attempt: {attempt + 1}: Network Error.")
    else:
        print("Failed after 3 attempts. ")
        return None 

    if response.status_code == 200:
        pokemon_data = response.json()

        required_fields = ['name', 'id', 'height', 'weight']

        if all(field in pokemon_data for field in required_fields):
            return Pokemon(
                name=pokemon_data['name'],
                id= pokemon_data['id'],
                height= pokemon_data['height'],
                weight= pokemon_data['weight']
            )
        else:
            print("Invalid API response")

    elif response.status_code == 404:
        print(f"Pokemon not Found. Error: {response.status_code}")

    elif response.status_code >= 500:
        print(f"PokeAPI server error. Try again later. Error: {response.status_code}")

    else:
        print(f"Failed to retrieve data {response.status_code}")