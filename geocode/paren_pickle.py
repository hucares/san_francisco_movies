#!/usr/bin/env python3
# eliminate any parenthesis
import pickle
import requests
import time

locations   = pickle.load(open('locations.p', 'rb'))
google_geo  = 'https://maps.googleapis.com/maps/api/geocode/json'
san_fran    = '37.76487,0122.41948'
index       = 0

index = 0
for loc in locations.keys():
    if locations[loc]['status'] == 'ZERO_RESULTS' \
        and loc is not None \
        and '(' in loc:

        print(index)
        index += 1
        time.sleep(.5)

        address = loc[loc.find("(")+1:loc.find(")")]

        payload     = {'address': address, 'bounds': san_fran, 'region': 'us'}
        r           = requests.get(google_geo, params = payload)

        locations[loc] = r.json()

        print(r.json())


pickle.dump(locations, open("locations.p", "wb"))
