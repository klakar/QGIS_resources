# -*- coding: utf-8 -*-
"""
**************************************************************************
*              User define expression functions for QGIS                 *
*                        to obtain the map extents                       *
*                                                                        *
*                             -------------------                        *
*       begin                : 2013-09-09                                *
*       copyright          : (C) 2013 by Alexandre Neto                  *
*       email                : senhor.neto@gmail.com                     *
*                                                                        *
*       update for QGIS3     : 2018-01-27                                *
*                              @klaskarlsson                             *
*                                                                        *
**************************************************************************

**************************************************************************
*                                                                        *
*   This program is free software; you can redistribute it and/or modify *
*   it under the terms of the GNU General Public License as published by *
*   the Free Software Foundation; either version 2 of the License, or    *
*   (at your option) any later version.                                  *
*                                                                        *
**************************************************************************
"""

from qgis.utils import qgsfunction, iface
from qgis.core import QgsProject

def map_bounds(layout_title):
    """
    Returns map bounds
    """
    my_layout = QgsProject.instance().layoutManager().layoutByName(layout_title)
    try:
        extent = my_layout.referenceMap().extent()
    except:
        extent = None
    
    return extent

@qgsfunction(args='auto', group='python')
def map_x_min(layout_title, feature, parent):
    """
    Returns the minimum x coordinate of the reference map from a specific composer.
    Calculations are in the Spatial Reference System of the project.<br>
    <h2>Syntax</h2>
    <p>map_x_min(layout_title)</p>
    <h2>Arguments</h2>
    <p>layout_title - is string. The title of the composer where the map is.</p>
    <h2>Example</h2>
    <p>map_x_min('my pretty map') -> -12345.679</p>
    """
    map_extent = map_bounds(layout_title)
    if map_extent:
        result = map_extent.xMinimum()
    else:
        result = None
    
    return result

@qgsfunction(args='auto', group='python')
def map_x_max(layout_title, feature, parent):
    """
    Returns the maximum x coordinate of the reference map from a specific composer.
    Calculations are in the Spatial Reference System of the project.<br>
    <h2>Syntax</h2>
    <p>map_x_max(layout_title)</p>
    <h2>Arguments</h2>
    <p>layout_title - is string. The title of the composer where the map is.</p>
    <h2>Example</h2>
    <p>map_x_max('my pretty map') -> 12345.679</p>
    """
    map_extent = map_bounds(layout_title)
    if map_extent:
        result = map_extent.xMaximum()
    else:
        result = None
    
    return result

@qgsfunction(args='auto', group='python')
def map_y_min(layout_title, feature, parent):
    """
    Returns the minimum y coordinate of the reference map from a specific composer.
    Calculations are in the Spatial Reference System of the project.<br>
    <h2>Syntax</h2>
    <p>map_y_min(layout_title)</p>
    <h2>Arguments</h2>
    <p>layout_title - is string. The title of the composer where the map is.</p>
    <h2>Example</h2>
    <p>map_y_min('my pretty map' -> -12345.679</p>
    """
    map_extent = map_bounds(layout_title)
    if map_extent:
        result = map_extent.yMinimum()
    else:
        result = None
    
    return result

@qgsfunction(args='auto', group='python')
def map_y_max(layout_title, feature, parent):
    """
    Returns the maximum y coordinate of the reference map from a specific composer.
    Calculations are in the Spatial Reference System of the project.<br>
    <h2>Syntax</h2>
    <p>map_y_max(layout_title)</p>
    <h2>Arguments</h2>
    <p>layout_title - is string. The title of the composer where the map is.</p>
    <h2>Example</h2>
    <p>map_y_max('my pretty map') -> 12345.679</p>
    """
    map_extent = map_bounds(layout_title)
    if map_extent:
        result = map_extent.yMaximum()
    else:
        result = None
    
    return result
