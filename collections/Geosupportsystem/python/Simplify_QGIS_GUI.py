#
# Beginner friendly QGIS GUI setup
# Start the Python console (ctrl+alt+P)
# Show the editor, load and run this script
#
showToolbars = "mFileToolBar mAttributesToolBar mDigitizeToolBar mHelpToolBar mMapNavToolBar mDataSourceManagerToolBar"
prev = None
for x in iface.mainWindow().findChildren(QToolBar): 
    if x.objectName() in showToolbars:
        x.setVisible(True)
        x.setIconSize(QSize(32,32))
    else:
        x.setVisible(False)
showDockWidgets = "Layers LayerStyling Browser"
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
