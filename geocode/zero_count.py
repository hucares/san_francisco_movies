#!/usr/bin/env python3
# count empty
import pickle
import time

locations   = pickle.load(open('locs.p', 'rb'))
zero_count = 0
for loc in locations.keys():
    if locations[loc] == '' or locations[loc]['status'] == 'ZERO_RESULTS':
        print(loc)
        zero_count += 1

print(zero_count)
