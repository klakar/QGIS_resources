##Add Advanced Labeling Fields To Selected Layer=name
from PyQt4.QtCore import QVariant
from qgis.utils import iface
from qgis.core import QgsField, QgsPalLayerSettings

# Function source: https://gis.stackexchange.com/a/216110/55741
def setColumnVisibility( layer, columnName, visible ):
    config = layer.attributeTableConfig()
    form = layer.editFormConfig()
    form.setWidgetType(layer.fieldNameIndex(columnName), "Hidden")
    columns = config.columns()
    for column in columns:
        if column.name == columnName:
            column.hidden = not visible
            break
    config.setColumns( columns )
    layer.setAttributeTableConfig( config )
    
lager = iface.activeLayer()
if not lager.isEditable():
    iface.actionToggleEditing().trigger()
lager.dataProvider().addAttributes([QgsField("Text_X", QVariant.Double, 'double', 10, 5),
QgsField("Text_Y", QVariant.Double, 'double', 10, 5), QgsField("Text_Ri", QVariant.Double, 'double', 3, 2), QgsField("Text_Vis", QVariant.Int, "", 3)])
lager.updateFields()
lager.commitChanges()
lager.setDefaultValueExpression(lager.fieldNameIndex("Text_Vis"), '1')
palager = QgsPalLayerSettings()
palager.readFromLayer(lager)
palager.enabled = True
palager.setDataDefinedProperty(QgsPalLayerSettings.PositionX, True, False, '', "Text_X")
palager.setDataDefinedProperty(QgsPalLayerSettings.PositionY, True, False, '', "Text_Y")
palager.setDataDefinedProperty(QgsPalLayerSettings.Rotation, True, False, '', "Text_Ri")
palager.setDataDefinedProperty(QgsPalLayerSettings.Show, True, False, '', "Text_Vis")
setColumnVisibility( lager, 'Text_X', False)
setColumnVisibility( lager, 'Text_Y', False)
setColumnVisibility( lager, 'Text_Ri', False)
setColumnVisibility( lager, 'Text_Vis', False)
palager.writeToLayer(lager)
rader = lager.getFeatures()
for rad in rader:
    rad['Text_Vis'] = 1
    lager.updateFeature(rad)
lager.commitChanges()
lager.startEditing()
iface.mapCanvas().refresh()
