import folium
import pandas as pd
from pandas import read_html
from flask import Flask
import numpy as np
from bs4 import BeautifulSoup

#Extract Table from Wikipedia Page
bridgelistdf = pd.read_html('CharlesRiverCrossings.html', header = 0, index_col = None, attrs = {'class':'wikitable'})[0]

#get rid of the NAN rows for coordinates
bridgelistdf.dropna(subset = ['Coordinates'], inplace = True)

#get list of bridge names
bridgenamesdf = bridgelistdf.loc[:, 'Crossing']

bridgenames = []
for bridgename in bridgenamesdf:
	bridgenames.append(bridgename)


#bridges I've run across
bridgesrun = ['Charlestown Bridge', 'MBTA Green Line Lechmere Viaduct', 'Longfellow Bridge', 'Harvard Bridge', 'Boston University Bridge', 'River Street Bridge', 'Western Avenue Bridge', 'John W. Weeks Bridge', 'Anderson Memorial Bridge', 'Eliot Bridge', 'Arsenal Street Bridge', 'North Beacon Street Bridge', 'Watertown Bridge', 'Cpl. Joseph U. Thompson Footbridge (new)', 'Bridge Street Bridge', 'Blue Heron Footbridge', 'Farwell Street Bridge', 'Mary T. Early Footbridge', 'Charles F. Graceffa Bridge', 'Elm Street Bridge', 'Richard Landry Park footbridge', 'Moody Street bridge', 'Gold Star Mothers Bridge', 'Footbridge from Riverside Rd., Newton to Recreation Rd., Weston', 'Riverside Park Footbridge']

#isolate the coordinates
coordinatesdf = bridgelistdf.loc[:, 'Coordinates']

lats = []
longs = []

#get list of coordinates as numbers
for coordinate in coordinatesdf:
		
	if("°N" in coordinate.split(" / ")[1].split(" ")[0]):
		lats.append(float(coordinate.split(" / ")[1].split(" ")[0].split("°N")[0].replace('\ufeff','')))

	if("°S" in coordinate.split(" / ")[1].split(" ")[0]):
		lats.append(-float(coordinate.split(" / ")[1].split(" ")[0].split("°S")[0].replace('\ufeff','')))

	if("°W" in coordinate.split(" / ")[1].split(" ")[1]):
		longs.append(-float(coordinate.split(" / ")[1].split(" ")[1].split("°W")[0].replace('\ufeff','')))

	if("°E" in coordinate.split(" / ")[1].split(" ")[1]):
		longs.append(float(coordinate.split(" / ")[1].split(" ")[1].split("°E")[0].replace('\ufeff','')))

if __name__ == "__main__":
	#Create Map
	m = folium.Map(location = [42.3736, -71.1097], zoom_start = 12)

	#create markers
	for i in range(len(lats)):
		pop = '<strong style="color:#967bb6;">' + bridgenames[i] + '</strong>'
		if(bridgenames[i] in bridgesrun):
			col = 'green'
		else:
			col = 'red'
		folium.Marker([lats[i], longs[i]], popup = pop, icon = folium.Icon(color = col)).add_to(m)

	m.save('charlesmap.html')



