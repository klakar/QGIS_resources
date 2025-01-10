"""
This script should be run from the Python console inside QGIS.

Download the file and OPEN the file in the Python console EDITOR.
It will not work if you copy and paste the code at the commandline.

It adds online sources to the QGIS Browser.
Each source should contain a list with the folowing items (string type):
[sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]

You can add or remove sources from the sources section of the code.

Script by Klas Karlsson
Sources from https://qms.nextgis.com/

Some services may require you to supply your own API key for the services to work.

Licence GPL-3

Regarding the terms of use for these background maps YOU will need to verify that you
follow the individual EULA that comes with the different services,
Most likely they will restrict how you can use the data.
Example:
For Esri basemaps you will need a valid ArcGIS online subscription to use the maps.

"""


# Sources
sources = []
sources.append(["xyz","Google Maps","","","","https://mt1.google.com/vt/lyrs=m&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D","","19","0"])
sources.append(["xyz","Google Satellite", "", "", "", "https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["xyz","Google Terrain", "", "", "", "https://mt1.google.com/vt/lyrs=t&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["xyz","Google Terrain Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=p&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["xyz","Google Satellite Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=y&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["xyz","Esri Boundaries Places", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["xyz","Esri Gray (dark)", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["xyz","Esri Gray (light)", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["xyz","Esri Hillshade", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Elevation/World_Hillshade/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "12", "0"])
sources.append(["xyz","Esri National Geographic", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "12", "0"])
sources.append(["xyz","Esri Navigation Charts", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Specialty/World_Navigation_Charts/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "12", "0"])
sources.append(["xyz","Esri Ocean", "", "", "Requires ArcGIS Onlinesubscription", "https://services.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "10", "0"])
sources.append(["xyz","Esri Physical Map", "", "", "Requires ArcGIS Onlinesubscription", "https://services.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "10", "0"])
sources.append(["xyz","Esri Satellite", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["xyz","Esri Shaded Relief", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["xyz","Esri Standard", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["xyz","Esri Terrain", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "13", "0"])
sources.append(["xyz","Esri Transportation", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["xyz","Esri Topo World", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["xyz","OpenStreetMap Standard", "", "", "OpenStreetMap contributors, under ODbL", "http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["xyz","OpenStreetMap H.O.T.", "", "", "OpenStreetMap contributors, under ODbL", "http://tile.openstreetmap.fr/hot/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["xyz","OpenTopoMap", "", "", "Kartendaten: © OpenStreetMap-Mitwirkende, SRTM | Kartendarstellung: © OpenTopoMap (CC-BY-SA)", "https://tile.opentopomap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "1"])
sources.append(["xyz","Strava All", "", "", "OpenStreetMap contributors, under ODbL", "https://heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["xyz","Strava Run", "", "", "OpenStreetMap contributors, under ODbL", "https://heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19", "", "15", "0"])
sources.append(["xyz","CartoDb Dark Matter", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/dark_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["xyz","CartoDb Dark Matter (No Labels)", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/dark_nolabels/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["xyz","CartoDb Positron", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/light_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["xyz","CartoDb Positron (No Labels)", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/light_nolabels/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["xyz","Bing VirtualEarth", "", "", "", "http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1", "", "19", "1"])



# Add sources to browser
for source in sources:
   connectionType = source[0]
   connectionName = source[1]
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/authcfg", source[2])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/password", source[3])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/referer", source[4])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/url", source[5])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/username", source[6])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/zmax", source[7])
   QSettings().setValue(f"connections/{connectionType}/items/{connectionName}/zmin", source[8])


# Update GUI
iface.reloadConnections()

# Message
print("Check the console for errors and restart QGIS.")
