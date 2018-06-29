import folium
map = folium.Map(location=[45.5236, -122.6750],tiles='Mapbox Bright',zoom_start = 6)

# to make our code more organized we use FeatureGroup

fg = folium.FeatureGroup(name = "My Map")

# using a for loop to add multiple markers

for coordinates in [[45.3288, -121.6625],[40.3288, -120.6625]]:
    fg.add_child(folium.Marker(coordinates,popup='Mt. Hood Meadows',icon=folium.Icon(icon='cloud', color='green')))



# fg.add_child(folium.Marker([40.3288, -120.6625],popup='Another Marker',icon=folium.Icon(icon='cloud', color='green')))

map.add_child(fg)

map.save("Map.html")

# map = folium.Map(location = [38.58, -99.09], zoom_start = 6 , tiles = "Mapbox Bright")
#
# map.add_child(folium.Marker(location = [38.2, -99.1],popup = "Hi i am a marker", icon = folium.Icon(color = 'green')))
#
# map.save("Map1.html")
