# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
*                                                                         *
*   Originally written by: @klaskarlsson                                  *
*   2019-09-25                                                            *
*                                                                         *
*   Fair warning: The code is cobbled togeather from googling and trial   *
*   and error. It is fragmented, probably bloated and possibly unstable.  *
*   You will run it at your own risk, but you will probably not break     *
*   your system....                                                       *
*   If you improve or clean the code up I'm interested to know.           *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from PyQt5.QtCore import QVariant
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField, 
                       QgsFields, QgsField,
                       QgsRectangle,
                       QgsFeatureRequest)
from qgis import processing


class PolygonGridNeighbours(QgsProcessingAlgorithm):
    """
    This algorithm is intended to be run on a polygon grid layer. It will add
    attributes for neighbouring polygons and populate them with values from
    a selected attribute.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    FIELD = 'FIELD'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return PolygonGridNeighbours()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'gridneighbours'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Grid Neighbours')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Vector table')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'vector_table'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        help_text = 'Add attributes for neighbouring polygons based on the selected '
        help_text += 'field in the grid polygon layer.\n'
        help_text += 'You can create a grid with the \"Create Grid\" processing tool.\n\n'
        help_text += 'Use the algorithm in your Atlas projects to indicate what '
        help_text += 'page is next to the current in different directions.'
        return self.tr(help_text)

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry, but it should be a polygon feature type for the algorithm to make sense
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        # We select a field from the input vector layer that is
        # used to populate the neighbour fields in the new layer
        self.addParameter(
            QgsProcessingParameterField(
                self.FIELD,
                self.tr('Identifying name field'),
                '',
                self.INPUT
            )
        )
        
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )
        
    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source, field and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )
        
        field = self.parameterAsFields(
            parameters,
            self.FIELD,
            context
        )

        # If source was not found, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSourceError method to return a standard
        # helper text for when a source cannot be evaluated
        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))
        
        # Adding new fields to the table. This is not trivial since we want to keep any current values in the table
        # The first step is here, where current source fields are concatinated with the new "neighbour" fields
        # Not sure why the code ended up here though. It would probably make more
        # sense to have it elseware...
        all_fields = source.fields()
        fields_list = ['neighbour_top', 'neighbour_topright', 'neighbour_right', 'neighbour_bottomright', 'neighbour_bottom', 'neighbour_bottomleft', 'neighbour_left', 'neighbour_topleft']
        for fn in fields_list:
            all_fields.append(QgsField(fn, QVariant.String))
            
        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            all_fields,
            source.wkbType(),
            source.sourceCrs()
        )
        
        
        # Send some information to the user (this is basically useless for the functionality)
        feedback.pushInfo('CRS is {}'.format(source.sourceCrs().authid()))

        # Compute the number of steps to display within the progress bar and
        # get features from source. But the algorithm should be pretty fast in
        # most use cases.
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        features = source.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            # Calculate for each feature a small rectangle just outside the bounds
            # of the polygon. Place this rectangle in a 2-dimensional list with the
            # names of the corresponding new attribute names.
            # This can probably be done much more streamlined, but I only found
            # reference to rectangles using the "setFilterRect()" function.
            fcenter = feature.geometry().centroid().asPoint() # the center of the current feature
            bbox = feature.geometry().boundingBox() # the extent of the current feature
            d = (bbox.xMaximum() - bbox.xMinimum()) / 100 # just a small fraction of feature size in the local CRS
            objekt_list = []
            objekt_list.append([fields_list[0], QgsRectangle(fcenter[0], bbox.yMaximum() + d, fcenter[0] + d, bbox.yMaximum() + 2 * d)])
            objekt_list.append([fields_list[1], QgsRectangle(bbox.xMaximum() + d, bbox.yMaximum() + d, bbox.xMaximum() + 2 * d, bbox.yMaximum() + 2 * d)])
            objekt_list.append([fields_list[2], QgsRectangle(bbox.xMaximum() + d, fcenter[1], bbox.xMaximum() + 2 * d, fcenter[1] + d)])
            objekt_list.append([fields_list[3], QgsRectangle(bbox.xMaximum() + d, bbox.yMinimum() - d, bbox.xMaximum() + 2 * d, bbox.yMinimum() - 2 * d)])
            objekt_list.append([fields_list[4], QgsRectangle(fcenter[0], bbox.yMinimum() - d, fcenter[0] + d, bbox.yMinimum() - 2 * d)])
            objekt_list.append([fields_list[5], QgsRectangle(bbox.xMinimum() - d, bbox.yMinimum() - d, bbox.xMinimum() - 2 * d, bbox.yMinimum() - 2 * d)])
            objekt_list.append([fields_list[6], QgsRectangle(bbox.xMinimum() - d, fcenter[1], bbox.xMinimum() - 2 * d, fcenter[1] + d)])
            objekt_list.append([fields_list[7], QgsRectangle(bbox.xMinimum() - d, bbox.yMaximum() + d, bbox.xMinimum() - 2 * d, bbox.yMaximum() + 2 * d)])
            
            # This is not very well documented but I found a reference in: https://gis.stackexchange.com/questions/219146/qgis-python-generate-index-field
            # Using the list with new attribute names and rectangles the layer
            # is filtered for polygons that intersect those rectangles.
            # The values in the selected source field is used to populate the new
            # fields in the attribute table.
            current_attributes = feature.attributes() # get the current attribute values in a list
            feature.setFields(all_fields) # set the new list of attributes for the feature. This clears all old values!!!
            for n, o in objekt_list:
                request = QgsFeatureRequest().setFilterRect(o)
                for f in source.getFeatures(request):
                    current_attributes.append(str(f[field[0]]))   # Add the new values to the "old" attribute values list
                    break
                else:   # Obscure Python feature is to use "else" in a block. It will only run if a "break" is not encountered in the block.
                    current_attributes.append('') # Add empty string to empty neighbouring locations.
            feature.setAttributes(current_attributes)  # Finally write the uppdated attribute values to the feature

            # Add a feature in the sink
            sink.addFeature(feature, QgsFeatureSink.FastInsert)            

            # Update the progress bar
            feedback.setProgress(int(current * total))
            
        # Return the results of the algorithm.
        return {self.OUTPUT: dest_id}


