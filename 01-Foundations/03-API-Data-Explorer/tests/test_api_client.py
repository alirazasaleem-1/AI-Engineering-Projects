from src.api_client import get_pokemon_info

def test_get_pokemon_info():
    pokemon = get_pokemon_info("pikachu")

    assert pokemon is not None 
    assert pokemon.name == 'pikachu'
    assert pokemon.id == 25