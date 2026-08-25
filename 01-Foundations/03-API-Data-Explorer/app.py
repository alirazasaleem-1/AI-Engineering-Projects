import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        pokemon_data = response.json()

        required_fields = ['name', 'id', 'height', 'weight']

        if all(field in pokemon_data for field in required_fields):
            return pokemon_data
        else:
            print("Invalid API response")

    elif response.status_code == 404:
        print(f"Pokemon not Found. Error: {response.status_code}")

    elif response.status_code >= 500:
        print(f"PokeAPI server error. Try again later. Error: {response.status_code}")

    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("Enter Pokemon name: ").strip().lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")