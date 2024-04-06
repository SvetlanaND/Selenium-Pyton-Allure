import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = 'a30b21a8f8fba1c865484dfad1e6fdfc'

def test_stastus_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2297})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2297})
    assert response.json()['data'][0]['trainer_name'] == 'KOTana'

