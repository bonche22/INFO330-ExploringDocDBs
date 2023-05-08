from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient('mongodb://localhost/pokemon')
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Query 1: Find all Pikachu
pikachu = pokemonColl.find({'Name': 'Pikachu'})
for result in pikachu:
    print(result)

# Query 2: Find all Pokemon with attack greater than 150
high_attack = pokemonColl.find({'Attack': {'$gt': 150}})
for result in high_attack:
    print(result)

# Query 3: Find all Pokemon with ability "Overgrow"
overgrow = pokemonColl.find({'Abilities': {'$in': ['Overgrow']}})
for result in overgrow:
    print(result)

# Close the MongoDB connection
mongoClient.close()
