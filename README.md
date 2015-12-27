# audiotour
Create an audio tour to explore an area by foot or by bike, generated from geojson

## What's required?

* python 2.7 
* pip install -r requirements.txt
* A {place}.json file defining your addresses and associated audiofiles for the audiotour
* a googlemaps geocoding API key

## How can I get a google API key?

1. Visit https://console.developers.google.com/apis/
2. Add a new project
3. Add a new key
4. Select the project and ensure you have enabled the googlemaps geocoding API
5. Open blank.config and rename to my.config
6. Set the api_key to your google API key

## How do I run this?

`$ python create_geojson.py {place}` where you have a file called `place`.json sitting in the same directory.

### Example

`$ python create_geojson.py hobart`

This will pick up data from `hobart.json` and create a geojson file called `hobart.geojson`  

## How do I create a map?

Use a mapping utility like mapbox.com

In mapbox classic you can create a nw mapbox editor project.

You can set the data  by importing the geojson file you have created with this script, and you can set the Title to name and Description to audiofile_list_html so the links show up.

### Example

https://a.tiles.mapbox.com/v4/mareebiketouroz.ohi50cjm/page.html?access_token=pk.eyJ1IjoibWFyZWViaWtldG91cm96IiwiYSI6Ijk5YjBkZDNmNzZkZTBkNzU3NThiNTRiZWM0NTFiNmM4In0.7tb_ZpOqSBUweCxL22qIeA#19/-42.88174/147.33230 