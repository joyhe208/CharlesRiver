import folium
import pandas as pd
from pandas import read_html

#Extract Table from Wikipedia Page
bridgelist = pd.read_html('CharlesRiverCrossings.html', header = 0, index_col = None, attrs = {'class':'wikitable'})[0]

coordinates = bridgelist.loc[:, 'Coordinates']
#print(coordinates.head(15))

#get list of coordinates as numbers
latitude = []
longitude = []

#Create Map
m = folium.Map(io = [42.3736, -71.1097], zoom_start = 12)
m.save('charlesmap.html')