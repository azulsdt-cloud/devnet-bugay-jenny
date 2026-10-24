import requests
import json

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
data = response.json()

pokemon_list = ["pikachu", "evee", "snorlax", "fennec", "bulbasaur"]
pokemon_height =[10, 20, 30, 40, 50]
pokemon_weight= [1, 2, 3, 4, 5]

name = pokemon[pokemon_list],
height = pokemon[pokemon_height],
weight = pokemon[pokemon_weight]

choice=input("Choose Pokemon: ")
choice = random.choice(pokemon_list)
response = response.json



r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"authenticated": true, ...'
r.json()
{'authenticated': True, ...}


