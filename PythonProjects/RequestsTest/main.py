import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd04a90fe40bdefdae595e8f14277b4a7'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "irinafurinova@yandex.ru",
    "password": "1506Vika"
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "273947",
    "name": "Гуся",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "273947"
}

'''response = requests.post(url= f'{URL}/trainers/reg', headers= HEADER, json=body_registration)
print(response.text)'''

'''response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json=body_create)
print(response_create.text)'''

'''response_change = requests.put(url= f'{URL}/pokemons', headers= HEADER, json=body_change)
print(response_change.text)'''

response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)