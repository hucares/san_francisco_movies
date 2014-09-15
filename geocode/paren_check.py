#!/usr/bin/env python3
# remove all locations not within sf
# or if zero results
import pickle
import requests
import time
import pdb


locations   = pickle.load(open('locs.p', 'rb'))
google_plc  = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
san_fran    = '37.76487,-122.41948'
key         = 'AIzaSyA1OP1vHLtzFX35YzyyBJqI7kTy6_dNDR0'
index       = 0

#contact google places on all non results
index = 0
for loc in locations.keys():
    print(locations[loc])
    if locations[loc]['status'] == 'ZERO_RESULTS' and ')' in loc:
        print(index)
        index += 1
        time.sleep(.65)

        address = loc[loc.find('(')+1:loc.find(')')]
        payload     = {'keyword': address, 'location': san_fran, 'radius': '13000', 'key': key}
        print(loc)
        r           = requests.get(google_plc, params = payload)
        locations[loc] = r.json()

        print(r.json())

pickle.dump(locations, open("locations.p", "wb"))
