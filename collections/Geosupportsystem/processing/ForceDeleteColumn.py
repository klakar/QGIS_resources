##Force Delete Table Column=name
##Vector_layer=vector
##Table_Field_to_Delete=field Vector_layer
# The script forcefully deletes named fields from a vector layer table.
# You get NO second chance, or opportunity to rollback.
# If you want that, you can use the much slower built in functions.

from qgis.core import QgsVectorLayer, QgsVectorDataProvider, QgsMapLayerRegistry, QgsMessageLog
QgsMessageLog.logMessage("Layer to process: %s" % Vector_layer, "ForceDelete")
QgsMessageLog.logMessage("Field to Force Delete: %s" % Table_Field_to_Delete, "ForceDelete")

vectorLayer = QgsVectorLayer(Vector_layer, 'TEMP', "ogr")
vectorLayer.isValid()
QgsMessageLog.logMessage("Getting Field Index for: %s" % Table_Field_to_Delete, "ForceDelete")
fieldID = vectorLayer.fieldNameIndex(Table_Field_to_Delete)
QgsMessageLog.logMessage("Deleting Field", "ForceDelete")
vectorLayer.dataProvider().deleteAttributes([fieldID])
vectorLayer.updateFields()
QgsMessageLog.logMessage("Reload Table...", "ForceDelete")
QgsMapLayerRegistry.instance().reloadAllLayers()