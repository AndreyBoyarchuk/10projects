import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
descr = list(data["NAME"])


def color_producer(elevation):
    if elevation < 1500:
        return 'red'
    elif 1500 <= elevation < 2000:
        return 'orange'
    else:
        return 'purple'


map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, ds in zip(lat, lon, elev, descr):
    fg.add_child(folium.Marker(location=[lt, ln], popup=(el, ds), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("Map1.html")
