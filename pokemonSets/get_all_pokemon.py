
import json

all_pokemon_set = open('all_pokemon.json')
all_pokemon = json.load(all_pokemon_set)

fossil={}
jungle={}
baseSet={}
for key, value in all_pokemon.items():
    if value['set']['name'] == 'Fossil':
        fossil[key] = value[]
print(json.dumps(fossil['Gambler']['images']['small'], indent=4))
    # print(all_pokemon[key]['images']['small'])