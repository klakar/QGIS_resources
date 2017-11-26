"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

import csv
fac_dict = {}
reader = csv.DictReader(open('Feature Description.csv'))
for row in reader:
    fac_dict[row['FAC_CODE']] = row['FAC_NAME']

@qgsfunction(args='auto', group='Custom')
def facc(fac_code, feature, parent):
    return fac_dict[fac_code]
