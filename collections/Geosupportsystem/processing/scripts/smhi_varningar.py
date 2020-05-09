from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterRasterDestination,
                       QgsVectorLayer,
                       QgsField,
                       QgsFeature,
                       QgsGeometry,
                       QgsProject)
import processing
import requests
import xml.etree.ElementTree as ET


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    Denna algoritm hämtar aktuella varningar från SMHI och skapar ett lager med dessa i QGIS.
    """

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        # Must return a new copy of your algorithm.
        return ExampleProcessingAlgorithm()

    def name(self):
        """
        Returns the unique algorithm name.
        """
        return 'smhivarningar'

    def displayName(self):
        """
        Returns the translated algorithm name.
        """
        return self.tr('Hämta varningar från SMHI')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to.
        """
        return self.tr('Väder')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs
        to.
        """
        return 'Varningar'

    def shortHelpString(self):
        """
        Returns a localised short help string for the algorithm.
        """
        return self.tr('Hämtar aktuella varningar från SMHI.')

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and outputs of the algorithm.
        """
             

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        
        smhi_alerts = 'https://opendata-download-warnings.smhi.se/api/version/2/alerts.xml'
        smhi_layers = 'https://opendata-download-warnings.smhi.se/api/version/2/districtviews/all.xml'
        root = ET.fromstring(requests.get(smhi_layers).text)
        alert_root = ET.fromstring(requests.get(smhi_alerts).text)

        vy = QgsVectorLayer("Polygon", "SMHI-Polygoner", "memory")
        crs = vy.crs()
        crs.createFromId(4326)
        vy.setCrs(crs)
        from qgis.PyQt.QtCore import QVariant
        py = vy.dataProvider()
        py.addAttributes([QgsField("fid", QVariant.Int),\
                        QgsField("sort", QVariant.Int),\
                        QgsField("category", QVariant.String),\
                        QgsField("name", QVariant.String),\
                        QgsField("event", QVariant.String),\
                        QgsField("priority", QVariant.Int),\
                        QgsField("level", QVariant.String),\
                        QgsField("color", QVariant.String),\
                        QgsField("description", QVariant.String)])
        vy.updateFields()


        for (fid, sort, category, name, geometry) in root.findall('{urn:se:smhi:cap:metadata}district_view'):
            fy = QgsFeature()
            y = QgsGeometry.fromWkt(geometry[1].text)
            y.get().swapXy()
            fy.setGeometry(y)
            fy.setAttributes([fid.text, \
                        sort.text, \
                        category.text, \
                        name.text])
            py.addFeature(fy)

        for alert in alert_root.iter('{urn:oasis:names:tc:emergency:cap:1.2}info'):
                for area in alert.iter('{urn:oasis:names:tc:emergency:cap:1.2}area'):
                    fid = int(area[0].text)
                attribs = { 4 : alert[7][1].text, \
                        5 : int(alert[8][1].text), \
                        6 : alert[9][1].text, \
                        7 : alert[10][1].text, \
                        8 : alert[17].text}
                vy.dataProvider().changeAttributeValues({ fid : attribs })



        vy.updateExtents() 
        QgsProject.instance().addMapLayer(vy)
        
        return {}