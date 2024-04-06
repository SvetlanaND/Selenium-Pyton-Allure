import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'a30b21a8f8fba1c865484dfad1e6fdfc'}
TOKEN = 'a30b21a8f8fba1c865484dfad1e6fdfc'

body_create = {
    "name": "Pypsichek1",
    "photo": "https://dolnikov.ru/pokemons/albums/079.png"
}

body_new_name = {
    "pokemon_id": "16045",
    "name": "Pypsichek2",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_in_pokeball = {
    "pokemon_id": "16045"
}


response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_new_name)

print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_create)

print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_in_pokeball)

print(response.text)
