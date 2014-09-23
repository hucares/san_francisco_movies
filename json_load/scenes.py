#!/usr/bin/env python3
# remove all locations not within sf
# or if zero results
import pickle
import json
import requests
import time
import pdb

json_data   = open('raw.json', encoding='utf-8').read()
data        = json.loads(json_data)
locations   = pickle.load(open('geocode/locs.p', 'rb'))
scenes      = data['data']

#places
rows = []

for scene in scenes:
    row = {}
    place = scene[10]

    row['title']    = scene[8]
    row['year']     = scene[9]
    row['location'] = place
    row['facts']    = scene[11]
    row['produc']   = scene[12]
    row['distrib']  = scene[13]
    row['director'] = scene[14]
    row['writer']   = scene[15]
    row['actor_1']  = scene[16]
    row['actor_1']  = scene[17]
    row['actor_1']  = scene[18]

    if locations[place]['status'] != 'ZERO_RESULTS':
        row['lat'] = locations[place]['results'][0]['geometry']['location']['lat']
        row['lng'] = locations[place]['results'][0]['geometry']['location']['lng']

    rows.append(row)

print(json.dumps(rows))
