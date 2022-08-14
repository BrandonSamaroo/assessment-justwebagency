import json

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
                actors[star]['Rating'] += float(movie['rating'])
    for actor in list(actors.keys()):
        if actors[actor]["Movies"] == 1:
            del actors[actor]
    actors = sorted(actors.items(), key = lambda x: (x[1]["Movies"]))
    for actor in actors:
        print("Star Name: " + actor[0] + "   /  Movies:  " + str(actor[1]["Movies"])  + "   /   AVG Rating:  " + str(round(actor[1]["Rating"]/actor[1]["Movies"],2)))
    data.close()