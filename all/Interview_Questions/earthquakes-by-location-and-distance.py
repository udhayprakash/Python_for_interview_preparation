"""
USGS (US Geological Survey) publishes various earthquake data as JSON feed. 
Here’s a feed spanning all domestic earthquakes from the past week: 
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
"""

# List of all places in CA.
# Sort list in ascending order based on distance

import requests 
import re

def getbylocation(locationname):
    URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
    response = requests.get(URL).json()
    earthquakes = set()
    for each in response['features']:
        if locationname in each['properties']['place']:
            earthquakes.add(each['properties']['place'].strip())
    print(len(earthquakes))

    locations = map(lambda locstr: re.search(f'(\d+)km .* of (.*), {locationname}', locstr).groups(), earthquakes)

    locations = sorted(locations, key = lambda x:(x[1], eval(x[0])))
    print(len(locations))
    return locations

for eachlocation in getbylocation('CA'):
    print(eachlocation)