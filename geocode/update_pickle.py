#!/usr/bin/env python3
import pickle
import requests
import time

locations   = pickle.load(open('locations.p', 'rb'))
google_geo  = 'https://maps.googleapis.com/maps/api/geocode/json'
san_fran    = '37.76487,0122.41948'
index       = 0

for loc in locations.keys():
    print(index)
    index += 1
    time.sleep(.5)

    payload     = {'address': loc, 'bounds': san_fran, 'region': 'us'}
    r           = requests.get(google_geo, params = payload)

    print(r.json())
    locations[loc] = r.json()

pickle.dump(locations, open("locations.p", "wb"))
