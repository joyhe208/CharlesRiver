import folium
import pandas as pd
from pandas import read_html

#Extract Table from Wikipedia Page
bridgelistdf = pd.read_html('CharlesRiverCrossings.html', header = 0, index_col = None, attrs = {'class':'wikitable'})[0]

#get rid of the NAN rows for coordinates
bridgelistdf.dropna(subset = ['Coordinates'], inplace = True)

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

#Create Map
m = folium.Map(location = [42.3736, -71.1097], zoom_start = 12)

#create markers
for i in range(len(lats)):
	folium.Marker([lats[i], longs[i]]).add_to(m)

m.save('charlesmap.html')