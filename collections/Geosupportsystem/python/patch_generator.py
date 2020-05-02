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
