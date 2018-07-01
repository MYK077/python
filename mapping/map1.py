import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

# ELEV in file is column name with elevation
elevation = list(data["ELEV"])

def color(elevation):

        if elevation < 1000:
            return 'green'
        elif 1000 < elevation <= 3000:
            return 'red'
        else:
            return 'orange'

map = folium.Map(location=[38.58, -99.09],tiles='Mapbox Bright',zoom_start = 4)

# to make our code more organized we use FeatureGroup
# creating feature group for volcanoes
fgv = folium.FeatureGroup(name ="Volcanoes")

# create feature group for population
fgp = folium.FeatureGroup(name ="Population")

# using a for loop to add multiple markers
for lat, lon, elev in zip(lat,lon,elevation):
    # fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(str(elev)+"m",parse_html = True),icon=folium.Icon(icon='cloud', color=color(elev))))

#Notice while using CircleMarker fill = True should be set for inside of circles to get colored.
    fgv.add_child(folium.CircleMarker(location=[lat,lon],radius = 6, popup = folium.Popup(str(elev)+"m",parse_html = True),color ='grey',fill = True,fill_color = color(elev), fill_opacity = 0.6 ))
#Geojson file has a data attribute in it
fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(),
style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
