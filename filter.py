import json

data = open('data.json')

movies = json.load(data)

print(movies[0])

data.close()