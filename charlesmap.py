import folium
from folium import IFrame
import pandas as pd
from pandas import read_html
from flask import Flask
import numpy as np
from bs4 import BeautifulSoup
import urllib.request
from charlesimages import *

#test
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
bridgesrun = ['Charlestown Bridge', 'MBTA Green Line Lechmere Viaduct', 'Longfellow Bridge', 'Harvard Bridge', 'Boston University Bridge', 'River Street Bridge', 'Western Avenue Bridge', 'John W. Weeks Bridge', 'Anderson Memorial Bridge', 'Eliot Bridge', 'Arsenal Street Bridge', 'North Beacon Street Bridge', 'Watertown Bridge', 'Cpl. Joseph U. Thompson Footbridge (new)', 'Bridge Street Bridge1', 'Blue Heron Footbridge', 'Farwell Street Bridge', 'Mary T. Early Footbridge', 'Charles F. Graceffa Bridge', 'Elm Street Bridge', 'Richard Landry Park footbridge', 'Moody Street bridge', 'Gold Star Mothers Bridge', 'Road bridge from Riverside Rd., Newton to Recreation Rd., Weston', 'Riverside Park Footbridge']

#isolate the coordinates
coordinatesdf = bridgelistdf.loc[:, 'Coordinates']

lats = []
longs = []

#get list of coordinates as numbers lol this makes me feel so hacky
for coordinate in coordinatesdf:
		
	if("°N" in coordinate.split(" / ")[1].split(" ")[0]):
		lats.append(float(coordinate.split(" / ")[1].split(" ")[0].split("°N")[0].replace('\ufeff','')))

	if("°S" in coordinate.split(" / ")[1].split(" ")[0]):
		lats.append(-float(coordinate.split(" / ")[1].split(" ")[0].split("°S")[0].replace('\ufeff','')))

	if("°W" in coordinate.split(" / ")[1].split(" ")[1]):
		longs.append(-float(coordinate.split(" / ")[1].split(" ")[1].split("°W")[0].replace('\ufeff','')))

	if("°E" in coordinate.split(" / ")[1].split(" ")[1]):
		longs.append(float(coordinate.split(" / ")[1].split(" ")[1].split("°E")[0].replace('\ufeff','')))

def dl_img(url, filename):
	path = "bridgeimages/" + filename + ".jpg"
	urllib.request.urlretrieve(url, path)

#prepare the html wiki page to get the images
#table_rows now has all the html stuff for each row as a list
html_doc = open('CharlesRiverCrossings.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.table	
table_rows = table.find_all('tr')
table_rows.remove(table_rows[4])
table_rows.remove(table_rows[0])

if __name__ == "__main__":
	#Create Map
	m = folium.Map(location = [42.3736, -71.1097], zoom_start = 12)

	#create markers
	for i in range(len(lats)):
		
		pophtml = '<strong style="color:#967bb6;">' + bridgenames[i] + '</strong><br>'

		if(bridgenames[i] in bridgesrun):
			col = 'green'

			pophtml = pophtml + '<img src= "bridgeimages/pic' + str(i) + '.jpg" style = "width: 100%;height: 100%;"/>'
		else:
			col = 'red'
		pop = folium.Popup(html = pophtml, max_width = "300", max_height = "300")
		folium.Marker([lats[i], longs[i]], popup = pop, icon = folium.Icon(color = col)).add_to(m)

	m.save('charlesmap.html')



