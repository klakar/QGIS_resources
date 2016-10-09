##Select objects within distance=name
##Select from layer=vector
##Within Distance=number0
##That are near Layer=vector
outputs_QGISFIXEDDISTANCEBUFFER_1=processing.runalg('qgis:fixeddistancebuffer', frnlager,somliggerinom,5.0,False,None)
outputs_QGISSELECTBYLOCATION_1=processing.runalg('qgis:selectbylocation', vljfrnlager,outputs_QGISFIXEDDISTANCEBUFFER_1['OUTPUT'],['within'],0.0,0,None)
