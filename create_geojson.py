#!/usr/bin/env python

"""
Reads a json file that conforms to json-schema places.json-schema
and creates a geojson file that conforms to places-geojson.json-schema
that can be used to display a map with places of interest and links
to audiofiles for an audiotour of an area of interest

Uses configuration in my.config 

TODO:
* define schema in places.json-schema
* define schema in places-geojson.json-schema
* enhance robustness w/ error checking
* schema conformity code 
"""

DEBUG = False

import geojson
import ConfigParser
import googlemaps
import json
import sys

if DEBUG:
	import pprint

## pick up command line arg
place = sys.argv[1]

## files used or created
places_json = "{place}.json".format(place=place)
audiotour_geojson = "{place}.geojson".format(place=place)
configfile = "my.config"

## read in api key
config = ConfigParser.ConfigParser()
config.read(configfile)
api_key = config.get("Google Developers", "api_key")

# set googlemaps api key
gmaps = googlemaps.Client(key=api_key)

# read in {place}.json as data
f = open(places_json)
data = json.load(f)
f.close()

# holds the list of geojson features created from our places of interest
features = []

for place in data['places']:
	## get lat lon from address
	geocode_result = gmaps.geocode("40 Macquarie St, Hobart TAS 7000")
	lat = geocode_result[0]['geometry']['location']['lat']
	lon = geocode_result[0]['geometry']['location']['lng']
	## create ul html of audiofiles
	audiofile_lis = []
	for audiofile in place["audiofiles"]:
		url = audiofile["url"]
		text = audiofile["text"]
		audiofile_li = "<li><a href=\"{url}\">{text}</a></li>".format(url=url, text=text)
		audiofile_lis.append(audiofile_li)
	ul = "<ul>{lis}</ul>".format(lis=''.join(audiofile_lis))
	place["audiofile_list_html"] = ul
	## create feature and append to list for geojson
	feature = geojson.Feature(geometry=geojson.Point((lon,lat)), properties=place)
	features.append(feature)

## output geojson	
featurecollection = geojson.FeatureCollection(features)
f = open(audiotour_geojson,'w')
if DEBUG:
	pprint.pprint(featurecollection)
geojson.dump(featurecollection, f, indent=4)
f.close()
print('Places geojson saved to %s' % audiotour_geojson)