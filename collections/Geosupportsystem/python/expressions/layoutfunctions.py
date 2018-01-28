# -*- coding: utf-8 -*-
"""
Functions to help in creating advanced layouts.
Adapted for QGIS 3

"""

from qgis.core import *
from qgis.gui import *

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
def mgrs_bigram(easting, northing, utm_z, feature, parent):
	"""
	Find MGRS bigram letters for 100 km square from E and N coordinate.<br>
	Based on map UTM projection in WGS-84.<br>
	<br><i>Only adapted to Northern Hemisphere</i>
	<h2>Example:</h2><br>
	<code>
	mgrs_bigram( 495395, 6392411, 33) -> 'VD'<br>
	<h2>Bigram for center of map with Item ID 'map'</h2><br>
	mgrs_bigram(x(map_get(item_variables('map'),'map_extent_center')),y(map_get(item_variables('map'),'map_extent_center')),to_int(right(map_get(item_variables('map'),'map_crs'),2)))
	</code>
	"""
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
def mgrs_gzd(easting, northing, utm_z, feature, parent): 
	"""
	Find MGRS Grid Zone Designator from E and N coordinate.<br>
	Based on map UTM projection in WGS-84.<br>
	<br><i>Only adapted to Northern Hemisphere</i>
	<h2>Example:</h2><br>
	<code>
	mgrs_gzd( 495395, 6392411, 33) -> '33V'<br><br>
	<h2>GZD for center of map with Item ID 'map'</h2><br>
	mgrs_gzd(x(map_get(item_variables('map'),'map_extent_center')),y(map_get(item_variables('map'),'map_extent_center')),to_int(right(map_get(item_variables('map'),'map_crs'),2)))
	</code>
	"""
	gzd_list = ['C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X'] 
	gzd_nr = (int(northing/888960) + 10)%20 
	gzd = str(utm_z) + gzd_list[gzd_nr] 
	return gzd
