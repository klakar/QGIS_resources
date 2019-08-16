from qgis.core import *
from qgis.gui import *

import random   # Needed for generating pseudo random numbers

@qgsfunction(args='auto', group='Geometry')
def random_points_in_polygon(number_of_points, feature, parent):
    """
    <i>random_points_in_polygon( n )</i><br><br>
    Generates 'n' number of points inside the current polygon geometry.<br><br>
    <b>Requires</b><br>
    <i>n</i> (Integer)<br><br>
    <b>Example</b><br>
    <i>random_points_in_polygon( 25 )</i><br>
    <br>
    &lt;geometry: MultiPoint&gt; with 25 points
    """
    points = list() # Create an empty list for the points
    
    
    # Until there's the required points in the list, loop (not the best way probably)
    while len(points) < number_of_points:
        # Create random x and y coordinates inside feature geometry bounding box
        rnd_x = random.uniform(feature.geometry().boundingBox().xMinimum(), feature.geometry().boundingBox().xMaximum())
        rnd_y = random.uniform(feature.geometry().boundingBox().yMinimum(), feature.geometry().boundingBox().yMaximum())
        # Use the coordinates to create a point
        rnd_point = QgsPointXY(rnd_x, rnd_y)
        
        # Test if the point is inside the feature geometry
        if QgsGeometry.fromPointXY(rnd_point).within(feature.geometry()):
            # If it is inside, add it to the list (increasing the length of the list)
            points.append(rnd_point)
    
    # Return a multipoint geometry
    return QgsGeometry.fromMultiPointXY(points)
