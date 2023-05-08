import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    pokemon1_score = 0
    pokemon2_score = 0

    # Compare the stats of the two pokemon and assign points accordingly
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1_score += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2_score += 1
        else:
            print("Both " + pokemon1['name'] + " and " + pokemon2['name'] + " have the same " + stat)

    # Determine the winner based on the total score
    if pokemon1_score > pokemon2_score:
        print("Battle results: " + pokemon1['name'])
    elif pokemon2_score > pokemon1_score:
        print("Battle results: " + pokemon2['name'])
    else:
        print("The battle is a tie!")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

if __name__ == "__main__":
    main()