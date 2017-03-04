"""
Try combining the functions in custom labels for two grids with 1000 meter interval lines.

first:

if(left(right( @grid_number , 4),1) = 0, 
if( @grid_axis = 'x', longNumber( @grid_number ), ''),
shortNumber( @grid_number ))

second:

if(left(right( @grid_number , 4),1) = 0, 
if( @grid_axis = 'y', longNumber( @grid_number ), ''),
'' )

Klas Karlsson

"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def shortNumber(gridNumber, feature, parent):
	"""
	Converts coordinates to "kilometer grid index".
	<h3>Example:</h3>
	<code>shortNumber(123456) -> '23'</code>
	<h3>Tips</h3>
	Try:
	<code>shortNumber( @grid_number )</code>
	"""
	gridString = str(int(gridNumber))
	return gridString[len(gridString)-5:len(gridString)-3]
	
	
@qgsfunction(args='auto', group='Custom')
def longNumber(gridNumber, feature, parent):
	"""
	Converts coordinates to "kilometer grid index" with superscript characters to create a "full" coordinate.
	<h3>Example:</h3>
	<code>longNumber(123456) -> '<sup>1</sup>23<sup>456</sup>'</code>
	<h3>Tips</h3>
	Try:
	<code>longNumber( @grid_number )</code>
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
