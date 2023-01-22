from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Layouts', referenced_columns=[])
def layout_map_extent(layout_name, map_name, feature, parent):
    """
    Collects the geometry (polygon) for the extent of a named map item in a named layout.
    <H2>Example usage:</H2>
    <ul><li>layout_map_extent('MyLayoutName', 'MyMapItemID') -&gt; <i>&lt;geometry: Polygon&gt;</i></li></ul>
    """
    map_extent = QgsRectangle
    project = QgsProject.instance()
    manager = project.layoutManager()
    layouts_list = manager.printLayouts()
    for layout in layouts_list:
        if layout.name() == layout_name:
            map_item = layout.itemById(map_name)
            map_extent = QgsGeometry.fromRect(map_item.extent())
            
    return map_extent
