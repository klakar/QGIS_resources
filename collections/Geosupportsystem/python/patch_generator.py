'''
Made by Klas Karlsson
Uses a polygon layer with suitable patch sized rectangles at representative areas.
The table must have three columns.
1. id
2. Label text (any name but [string])
3. Rotation (if you want to tweak the patch [float] should be default 0.0)

Before you run the script from the python consol in QGIS:
- Turn the layer visibility off (unless you want to show it in the patches)
- Have the patch layer selected (the script is run on the active layer)
- Save the project somewhere (patches are generated at this location)

The script generates lines with HTML in the Python consol. Copy this code!

In the layout, add a HTML frame and paste the code as source.

Style the apperance with css in the "User Stylesheet" settings:

******** Example CSS **********
.patch {
   width: 110px;
}
.title {
   font-family: Arial; 
   font-size: 12pt;
   text-align: left;
   padding: 0px 16px;
}
table {
   border-spacing: 0px 4px;
}
body {
   margin: 0;
}
*******************************

You can tweak the HTML code if you want multiple columns. It's not that hard.
'''
import re

layer = iface.activeLayer()
features = layer.getFeatures()

patch_width = 300
patches = []
titles = []

for feature in features:
   print(feature[1])
   geom = feature.geometry()
   image_location = os.path.join(QgsProject.instance().homePath(), re.sub(r'(?u)[^-\w.]', '', feature[1]) + ".png")
   patches.append(image_location)
   titles.append(feature[1])
   layers = iface.mapCanvas().layers()
   settings = QgsMapSettings()
   settings.setLayers(layers)
   patch_height = patch_width * geom.boundingBox().height() / geom.boundingBox().width()
   settings.setOutputSize(QSize(patch_width, patch_height))
   settings.setRotation(feature[2])
   settings.setExtent(geom.boundingBox())

   render = QgsMapRendererParallelJob(settings)

   def finished():
      img = render.renderedImage()
      img.save(image_location, "png")

   render.finished.connect(finished)
   render.start()
   render.waitForFinished()

html_string = '<html><body><table>\n'   
for (patch, title) in zip(patches, titles):
    html_string += '<tr><td><img class="patch" src="%s"></td><td><p class="title">%s</p></td></tr>\n' % (patch, title)
    
html_string += '</table></body></html>'
print(html_string)
