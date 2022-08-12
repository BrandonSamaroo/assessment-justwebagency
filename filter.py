import json
import sys

def printActors():
    data = open('data.json')
    movies = json.load(data)
    actors = {}
    for movie in movies:
        stars = movie['stars'].split(", ")
        for star in stars:
            if star not in actors:
                actors[star] = {'Movies': 1, 'Rating': float(movie['rating'])}
            else:
                actors[star]['Movies'] += 1
                actors[star]['Rating'] = actors[star]['Rating'] + float(movie['rating'])
    for actor in list(actors.keys()):
        if actors[actor]["Movies"] == 1:
            del actors[actor]
    print(actors)
    data.close()