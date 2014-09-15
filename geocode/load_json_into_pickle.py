# loads unique locations into dictionary into pickle

import json
import pickle

json_data   = open('raw.json', encoding='utf-8').read()
data        = json.loads(json_data)

scenes      = data['data']
locations   = {}

for scene in scenes:
    address = scene[10]
    locations[address] = ''

pickle.dump(locations, open("locs.p", "wb"))
