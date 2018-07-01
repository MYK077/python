import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
# ELEV in file is column name with elevation
elevation = list(data["ELEV"])

map = folium.Map(location=[38.58, 99.09],tiles='Mapbox Bright',zoom_start = 4)
# to make our code more organized we use FeatureGroup

fg = folium.FeatureGroup(name ="My Map")

# using a for loop to add multiple markers

for lat, lon, elev in zip(lat,lon,elevation):
    fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(str(elev)+"m",parse_html = True),icon=folium.Icon(icon='cloud', color='green')))



# fg.add_child(folium.Marker([40.3288, -120.6625],popup='Another Marker',icon=folium.Icon(icon='cloud', color='green')))

map.add_child(fg)

map.save("Map1.html")

# map = folium.Map(location = [38.58, -99.09], zoom_start = 6 , tiles = "Mapbox Bright")
#
# map.add_child(folium.Marker(location = [38.2, -99.1],popup = "Hi i am a marker", icon = folium.Icon(color = 'green')))
#
# map.save("Map1.html")
