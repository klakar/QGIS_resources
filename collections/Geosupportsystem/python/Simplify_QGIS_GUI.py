#
# Beginner friendly QGIS GUI setup
# Start the Python console (ctrl+alt+P)
# Show the editor, load and run this script
#

# List toolbars to make visible (all others will be hidden)
showToolbars = "mFileToolBar mAttributesToolBar mDigitizeToolBar mHelpToolBar mMapNavToolBar mDataSourceManagerToolBar"

# Go through all toolbars
for x in iface.mainWindow().findChildren(QToolBar): 
    if x.objectName() in showToolbars:
        x.setVisible(True)
        x.setIconSize(QSize(32,32))
    else:
        x.setVisible(False)

# List panels to make visible (all others will be hidden)
showDockWidgets = "Layers LayerStyling Browser"

# Go through all panels and place some of them at specific locations
prev = None
for d in iface.mainWindow().findChildren(QDockWidget): 
    if d.objectName() in showDockWidgets:
        if d.objectName() in "Browser LayerStyling":
            iface.addDockWidget(Qt.RightDockWidgetArea,d)
            if prev:
                iface.mainWindow().tabifyDockWidget(prev,d)
            prev = d
        if d.objectName() in "Layers":
            iface.addDockWidget(Qt.LeftDockWidgetArea,d)
        d.setVisible(True)
    else:
        d.setVisible(False)
