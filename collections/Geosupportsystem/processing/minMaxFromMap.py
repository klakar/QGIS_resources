"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import QGis
from qgis.gui import *
from qgis.utils import qgsfunction, iface


def map_bounds(composer_title, map_id):
 """
 Returns a rectangle with the bounds of a map
 from a specific composer
 """
 composers = iface.activeComposers()
 for composer_view in composers:
  composer_window = composer_view.composerWindow()
  window_title = composer_window.windowTitle()
  if window_title == composer_title:
   composition = composer_view.composition()
   map = composition.getComposerMapById(map_id)
   if map:
    extent = map.currentMapExtent()
    break
 else:
  extent = None
 
 return extent

@qgsfunction(2,"python")
def map_x_min(values, feature, parent):
 """
 Returns the minimum x coordinate of a map from a specific composer.
 Calculations are in the Spatial Reference System of the project.
 
<h2>Syntax</h2>
 
map_x_min(composer_title, map_id)
 
<h2>Arguments</h2>
 
composer_title - is string. The title of the composer where the map is.
 map_id - integer. The id of the map.
 
<h2>Example</h2>
 
map_x_min('my pretty map', 0) -> -12345.679
 
 """
 composer_title = values[0]
 map_id = values[1]
 map_extent = map_bounds(composer_title, map_id)
 if map_extent:
  result = map_extent.xMinimum()
 else:
  result = None
 
 return result
 
@qgsfunction(2,"python")
def map_x_max(values, feature, parent):
 """
 Returns the maximum x coordinate of a map from a specific composer.
 Calculations are in the Spatial Reference System of the project.
 
<h2>Syntax</h2>
 
map_x_max(composer_title, map_id)
 
<h2>Arguments</h2>
 
composer_title - is string. The title of the composer where the map is.
 map_id - integer. The id of the map.
 
<h2>Example</h2>
 
map_x_max('my pretty map', 0) -> 12345.679
 
 """
 composer_title = values[0]
 map_id = values[1]
 map_extent = map_bounds(composer_title, map_id)
 if map_extent:
  result = map_extent.xMaximum()
 else:
  result = None
 
 return result
 
@qgsfunction(2,"python")
def map_y_min(values, feature, parent):
 """
 Returns the minimum y coordinate of a map from a specific composer.
 Calculations are in the Spatial Reference System of the project.
 
<h2>Syntax</h2>
 
map_y_min(composer_title, map_id)
 
<h2>Arguments</h2>
 
composer_title - is string. The title of the composer where the map is.
 map_id - integer. The id of the map.
 
<h2>Example</h2>
 
map_y_min('my pretty map', 0) -> -12345.679
 
 """
 composer_title = values[0]
 map_id = values[1]
 map_extent = map_bounds(composer_title, map_id)
 if map_extent:
  result = map_extent.yMinimum()
 else:
  result = None
 
 return result
 
@qgsfunction(2,"python")
def map_y_max(values, feature, parent):
 """
 Returns the maximum y coordinate of a map from a specific composer.
 Calculations are in the Spatial Reference System of the project.
 
<h2>Syntax</h2>
 
map_y_max(composer_title, map_id)
 
<h2>Arguments</h2>
 
composer_title - is string. The title of the composer where the map is.
 map_id - integer. The id of the map.
 
<h2>Example</h2>
 
map_y_max('my pretty map', 0) -> 12345.679
 
 """
 composer_title = values[0]
 map_id = values[1]
 map_extent = map_bounds(composer_title, map_id)
 if map_extent:
  result = map_extent.yMaximum()
 else:
  result = None
 
 return result
