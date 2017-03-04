"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def skala(kart_id, feature, parent):
	layouts = iface.activeComposers()
	for layout_vy in layouts:
		layout_ruta = layout_vy.composerWindow()
		layout_nu = layout_vy.composition()
		karta = layout_nu.getComposerMapById(kart_id)
		if karta:
			skala = int(karta.scale())
	return skala
