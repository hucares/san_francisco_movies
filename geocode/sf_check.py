#!/usr/bin/env python3
# remove all locations not within sf
# or if zero results
import pickle
import requests
import time
import pdb


locations   = pickle.load(open('locations.p', 'rb'))
google_plc  = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
san_fran    = '37.76487,-122.41948'
key         = 'AIzaSyA1OP1vHLtzFX35YzyyBJqI7kTy6_dNDR0'
index       = 0

#clean out all non results
for loc in locations.keys():
    if locations[loc]['status'] == 'ZERO_RESULTS':
        locations[loc] = ''
    elif locations[loc]['status'] != 'ZERO_RESULTS' \
            and loc is not None:

        def long_name(x): return x['long_name'] == 'San Francisco'

        components = locations[loc]['results'][0]['address_components']
        if not any(list(map(long_name, components))):
            locations[loc] = ''

#contact google places on all non results
index = 0
for loc in locations.keys():

    if locations[loc] == '':
        print(index)
        index += 1
        time.sleep(.5)

        payload     = {'keyword': loc, 'location': san_fran, 'radius': '10000', 'key': key}
        print(loc)
        r           = requests.get(google_plc, params = payload)
        locations[loc] = r.json()

        print(r.json())

pickle.dump(locations, open("locations.p", "wb"))
