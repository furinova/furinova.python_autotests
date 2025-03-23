import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd04a90fe40bdefdae595e8f14277b4a7'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22741'


def test_code():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Irina001'