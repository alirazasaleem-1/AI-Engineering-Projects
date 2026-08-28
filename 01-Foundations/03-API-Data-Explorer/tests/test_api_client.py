from src.api_client import get_pokemon_info

def test_get_pokemon_info():
    pokemon = get_pokemon_info("pikachu")

    assert pokemon is not None 
    assert pokemon.name == 'pikachu'
    assert pokemon.id == 25

def test_invalid_pokemon():
    pokemon = get_pokemon_info("this-pokemon-does-not-exist")

    assert pokemon is None

