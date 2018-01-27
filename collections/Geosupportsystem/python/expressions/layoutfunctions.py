# -*- coding: utf-8 -*-
"""
Functions to help in creating advanced layouts.
Adapted for QGIS 3

'ref' functions based on work by Alexandre Neto (GPL)

Created By @klaskarlsson Klas Karlsson
Licence: GPLv3

"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Advanced Layout')
def ref_x_min(layout_title, feature, parent):
	"""
	Calculate the minimum and maximum coordinat of the reference map extents
	in the named layout.
	<h2>Example usage:</h2>
	<ul>
		<li>ref_x_min('my layout') -> 495395.1285</li>
		<li>ref_y_max('my layout') -> 6392411.4585</li>
	</ul>
	<h2>
	To create a "corner label" try the folowing code:
	</h2><br>
	<code>
	'E ' || to_int(ref_x_min('layout_name')) || '\\nN ' || to_int(ref_y_min('layout_name'))
	</code>
	"""
	calc_x_min = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap().extent().xMinimum()
	return calc_x_min

@qgsfunction(args='auto', group='Advanced Layout')
def ref_x_max(layout_title, feature, parent):
	"""
	Calculate the minimum and maximum coordinat of the reference map extents
	in the named layout.
	<h2>Example usage:</h2>
	<ul>
		<li>ref_x_min('my layout') -> 495395.1285</li>
		<li>ref_y_max('my layout') -> 6392411.4585</li>
	</ul>
	<h2>
	To create a "corner label" try the folowing code:
	</h2><br>
	<code>
	'E ' || to_int(ref_x_min('layout_name')) || '\\nN ' || to_int(ref_y_min('layout_name'))
	</code>
	"""
	calc_x_max = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap().extent().xMaximum()
	return calc_x_max

@qgsfunction(args='auto', group='Advanced Layout')
def ref_y_min(layout_title, feature, parent):
	"""
	Calculate the minimum and maximum coordinat of the reference map extents
	in the named layout.
	<h2>Example usage:</h2>
	<ul>
		<li>ref_x_min('my layout') -> 495395.1285</li>
		<li>ref_y_max('my layout') -> 6392411.4585</li>
	</ul>
	<h2>
	To create a "corner label" try the folowing code:
	</h2><br>
	<code>
	'E ' || to_int(ref_x_min('layout_name')) || '\\nN ' || to_int(ref_y_min('layout_name'))
	</code>
	"""
	calc_y_min = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap().extent().yMinimum()
	return calc_y_min

@qgsfunction(args='auto', group='Advanced Layout')
def ref_y_max(layout_title, feature, parent):
	"""
	Calculate the minimum and maximum coordinat of the reference map extents
	in the named layout.
	<h2>Example usage:</h2>
	<ul>
		<li>ref_x_min('my layout') -> 495395.1285</li>
		<li>ref_y_max('my layout') -> 6392411.4585</li>
	</ul>
	<h2>
	To create a "corner label" try the folowing code:
	</h2><br>
	<code>
	'E ' || to_int(ref_x_min('layout_name')) || '\\nN ' || to_int(ref_y_min('layout_name'))
	</code>
	"""
	calc_y_max = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap().extent().yMaximum()
	return calc_y_max
	
"""
Functions to be used with grid coordinates (mostly)
"""

@qgsfunction(args='auto', group='Advanced Layout')
def utm_short(gridNumber, feature, parent):
	"""
	Converts coordinates to "kilometer grid index".
	<h3>Example:</h3>
	<code>utm_short(123456) -> '23'</code>
	<h3>Tips</h3>
	Try:
	<code>utm_short( @grid_number )</code>
	"""
	gridString = str(int(gridNumber))
	return gridString[len(gridString)-5:len(gridString)-3]
	
	
@qgsfunction(args='auto', group='Advanced Layout')
def utm_long(gridNumber, feature, parent):
	"""
	Converts coordinates to "kilometer grid index" with superscript characters to create a "full" coordinate.
	<h3>Example:</h3>
	<code>utm_long(123456) -> '<sup>1</sup>23<sup>456</sup>'</code>
	<h3>Tips</h3>
	Try:
	<code>utm_long( @grid_number )</code>
	<h3>Unicode Font</h3>
	You need to select a font that supports unicode for this to work.
	"""
	gridString = str(int(gridNumber))
	fullString = ''
	supScr = (u'\u2070',u'\u00B9',u'\u00B2',u'\u00B3',u'\u2074',u'\u2075',u'\u2076',u'\u2077',u'\u2078',u'\u2079')
	charNumber = len(gridString)
	for char in gridString:
		if charNumber == 5 or charNumber == 4:
			fullString += char
		else:
			fullString += supScr[int(char)]
		charNumber -= 1
	
	return fullString

@qgsfunction(args='auto', group='Advanced Layout')
def utm_index(gridNumber, feature, parent):
	"""
	Converts coordinates to "kilometer grid index" with superscript characters to create a label with 100 km "index" number.
	<h3>Example:</h3>
	<code>utm_index(123456) -> '<sup>1</sup>23'</code>
	<h3>Tips</h3>
	Try:
	<code>utm_index( @grid_number )</code>
	<h3>Unicode Font</h3>
	You need to select a font that supports unicode for this to work.
	"""
	gridString = str(int(gridNumber))
	fullString = ''
	supScr = (u'\u2070',u'\u00B9',u'\u00B2',u'\u00B3',u'\u2074',u'\u2075',u'\u2076',u'\u2077',u'\u2078',u'\u2079')
	charNumber = len(gridString)
	for char in gridString:
		if charNumber == 5 or charNumber == 4:
			fullString += char
		if charNumber >= 6:
			fullString += supScr[int(char)]
		charNumber -= 1
	
	return fullString
	
"""
Functions for MGRS lettering based on UTM easting/northing coordinates.
"""

from qgis.utils import iface 
@qgsfunction(args='auto', group='Advanced Layout') 
def mgrs_bigram(easting, northing, layout_title, feature, parent):
	"""
	Find MGRS bigram letters for 100 km square from E and N coordinate.<br>
	Based on map UTM projection in WGS-84. (EPSG:32601 - EPSG:32960).<br>
	<br><i>Only adapted to Northern Hemisphere</i>
	<h2>Example:</h2><br>
	<code>
	mgrs_bigram( 495395, 6392411, 'layout_title') -> 'VD'
	</code>
	"""
	reference_map = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap()
	epsg_code = reference_map.crs().authid() 
	utm_z = int(epsg_code[-2:]) 
	mgrs_col = utm_z%3 
	col_type_list = [['S','T','U','V','W','X','Y','Z'],['A','B','C','D','E','F','G','H'],['K','L','M','N','P','Q','R']] 
	col_100k = int(easting/100000)-1 
	mgrs_row = utm_z%2 
	row_list = ['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V'] 
	if mgrs_row == 0: 
		eq_offset = 5 
	else: 
		eq_offset = 0 
	row_100k = (int(northing/100000) + eq_offset)%20 
	bigram = col_type_list[mgrs_col][col_100k] + row_list[row_100k] 
	return bigram

@qgsfunction(args='auto', group='Advanced Layout') 
def mgrs_gzd(easting, northing, layout_title, feature, parent): 
	"""
	Find MGRS Grid Zone Designator from E and N coordinate.<br>
	Based on map UTM projection in WGS-84. (EPSG:32601 - EPSG:32960).<br>
	<br><i>Only adapted to Northern Hemisphere</i>
	<h2>Example:</h2><br>
	<code>
	mgrs_bigram( 495395, 6392411, 'layout_title') -> 'VD'
	</code>
	"""
	reference_map = QgsProject.instance().layoutManager().layoutByName(layout_title).referenceMap()
	epsg_code = reference_map.crs().authid() 
	utm_z = int(epsg_code[-2:]) 
	gzd_list = ['C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X'] 
	gzd_nr = (int(northing/888960) + 10)%20 
	gzd = str(utm_z) + gzd_list[gzd_nr] 
	return gzd
