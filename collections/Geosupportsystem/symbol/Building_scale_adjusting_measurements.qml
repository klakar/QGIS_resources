<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.4.0-Madeira" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" maxScale="-4.65661e-10" simplifyDrawingTol="1" labelsEnabled="1" simplifyLocal="1" simplifyMaxScale="1" simplifyDrawingHints="1" readOnly="0" minScale="1e+8" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" symbollevels="0" forceraster="0" enableorderby="0">
    <symbols>
      <symbol clip_to_extent="1" type="fill" name="0" alpha="1">
        <layer locked="1" enabled="1" class="GeometryGenerator" pass="0">
          <prop v="Line" k="SymbolType"/>
          <prop v="offset_curve( segments_to_lines( $geometry ) , 8 )" k="geometryModifier"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if( @map_scale &lt; 2500, 1, 0)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" type="line" name="@0@0" alpha="1">
            <layer locked="0" enabled="1" class="ArrowLine" pass="0">
              <prop v="1" k="arrow_start_width"/>
              <prop v="MM" k="arrow_start_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
              <prop v="0" k="arrow_type"/>
              <prop v="0.2" k="arrow_width"/>
              <prop v="MM" k="arrow_width_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
              <prop v="1.9" k="head_length"/>
              <prop v="MapUnit" k="head_length_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
              <prop v="0.5" k="head_thickness"/>
              <prop v="MapUnit" k="head_thickness_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
              <prop v="2" k="head_type"/>
              <prop v="1" k="is_curved"/>
              <prop v="1" k="is_repeated"/>
              <prop v="0" k="offset"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="fill" name="@@0@0@0" alpha="1">
                <layer locked="0" enabled="1" class="SimpleFill" pass="0">
                  <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
                  <prop v="0,0,0,255" k="color"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="no" k="outline_style"/>
                  <prop v="0.26" k="outline_width"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="solid" k="style"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
            <layer locked="0" enabled="1" class="MarkerLine" pass="0">
              <prop v="3" k="interval"/>
              <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
              <prop v="MM" k="interval_unit"/>
              <prop v="0" k="offset"/>
              <prop v="0" k="offset_along_line"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
              <prop v="MM" k="offset_along_line_unit"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="vertex" k="placement"/>
              <prop v="1" k="rotate"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="marker" name="@@0@0@1" alpha="1">
                <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
                  <prop v="0" k="angle"/>
                  <prop v="255,0,0,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="line" k="name"/>
                  <prop v="0,3.49999999999999956" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MapUnit" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="9" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MapUnit" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
        <layer locked="1" enabled="1" class="GeometryGenerator" pass="0">
          <prop v="Marker" k="SymbolType"/>
          <prop v="nodes_to_points( $geometry)" k="geometryModifier"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if( @map_scale &lt; 2500, 1, 0)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" type="marker" name="@0@1" alpha="1">
            <layer locked="0" enabled="1" class="GeometryGenerator" pass="0">
              <prop v="Line" k="SymbolType"/>
              <prop v="make_line( point_n( $geometry,(@geometry_part_num)),point_n( $geometry,(@geometry_part_num+1)))" k="geometryModifier"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" type="line" name="@@0@1@0" alpha="1">
                <layer locked="0" enabled="1" class="MarkerLine" pass="0">
                  <prop v="3" k="interval"/>
                  <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
                  <prop v="MM" k="interval_unit"/>
                  <prop v="-10.8" k="offset"/>
                  <prop v="0" k="offset_along_line"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
                  <prop v="MM" k="offset_along_line_unit"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MapUnit" k="offset_unit"/>
                  <prop v="centralpoint" k="placement"/>
                  <prop v="1" k="rotate"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" name="name" value=""/>
                      <Option name="properties"/>
                      <Option type="QString" name="type" value="collection"/>
                    </Option>
                  </data_defined_properties>
                  <symbol clip_to_extent="1" type="marker" name="@@@0@1@0@0" alpha="1">
                    <layer locked="0" enabled="1" class="FontMarker" pass="0">
                      <prop v="0" k="angle"/>
                      <prop v="A" k="chr"/>
                      <prop v="0,0,0,255" k="color"/>
                      <prop v="Ubuntu Condensed" k="font"/>
                      <prop v="1" k="horizontal_anchor_point"/>
                      <prop v="bevel" k="joinstyle"/>
                      <prop v="0,0" k="offset"/>
                      <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                      <prop v="MM" k="offset_unit"/>
                      <prop v="35,35,35,255" k="outline_color"/>
                      <prop v="0" k="outline_width"/>
                      <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                      <prop v="MM" k="outline_width_unit"/>
                      <prop v="4" k="size"/>
                      <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                      <prop v="MapUnit" k="size_unit"/>
                      <prop v="1" k="vertical_anchor_point"/>
                      <data_defined_properties>
                        <Option type="Map">
                          <Option type="QString" name="name" value=""/>
                          <Option type="Map" name="properties">
                            <Option type="Map" name="angle">
                              <Option type="bool" name="active" value="true"/>
                              <Option type="QString" name="expression" value="CASE WHEN azimuth(&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)),&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)+1)&#xa;&#x9;)> pi()  THEN degrees(azimuth(&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)),&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)+1)&#xa;&#x9;))+90+ @map_rotation &#xa;&#x9;ELSE&#xa;&#x9;degrees(azimuth(&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)),&#xa;&#x9;&#x9;point_n( $geometry,(@geometry_part_num)+1)&#xa;&#x9;))-90+ @map_rotation &#xa;&#x9;END"/>
                              <Option type="int" name="type" value="3"/>
                            </Option>
                            <Option type="Map" name="char">
                              <Option type="bool" name="active" value="true"/>
                              <Option type="QString" name="expression" value="format_number(length(make_line( point_n( $geometry,(@geometry_part_num)),point_n( $geometry,(@geometry_part_num+1)))),2)||' m'"/>
                              <Option type="int" name="type" value="3"/>
                            </Option>
                          </Option>
                          <Option type="QString" name="type" value="collection"/>
                        </Option>
                      </data_defined_properties>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" enabled="1" class="SimpleFill" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="250,250,250,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.5" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="fillColor">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if( @map_scale >= 2500, '#000000',  @symbol_color )"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style multilineHeight="1" previewBkgrdColor="#ffffff" blendMode="0" fontUnderline="0" fieldName="format_number(area($geometry),0)||' m²'" fontWordSpacing="0" fontStrikeout="0" fontCapitals="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" fontLetterSpacing="0" useSubstitutions="0" textColor="0,0,0,255" fontSize="3" namedStyle="Italic" fontFamily="Arial" isExpression="1" fontSizeUnit="MapUnit" textOpacity="1" fontItalic="1">
        <text-buffer bufferSize="1" bufferSizeUnits="MM" bufferDraw="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0"/>
        <background shapeOffsetY="0" shapeSizeUnit="MapUnit" shapeOffsetX="0" shapeBorderWidth="0" shapeSizeX="3.1" shapeSVGFile="" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="1" shapeSizeY="1.1" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="2.5" shapeOffsetUnit="MM" shapeOpacity="0.201" shapeRadiiY="2.4" shapeBorderColor="128,128,128,255" shapeDraw="1" shapeSizeType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeRadiiUnit="MapUnit" shapeJoinStyle="128" shapeRotationType="0" shapeFillColor="255,255,255,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeBorderWidthUnit="MM"/>
        <shadow shadowDraw="0" shadowBlendMode="6" shadowOpacity="0.7" shadowOffsetUnit="MM" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowRadiusUnit="MM" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowColor="0,0,0,255" shadowRadiusAlphaOnly="0"/>
        <substitutions/>
      </text-style>
      <text-format decimals="3" wrapChar="" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" plussign="0" addDirectionSymbol="0" rightDirectionSymbol=">" reverseDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" multilineAlign="4294967295"/>
      <placement priority="5" repeatDistanceUnits="MM" fitInPolygonOnly="1" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" distUnits="MM" dist="0" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" placement="4" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="0" rotationAngle="0" offsetType="0" xOffset="0" quadOffset="4" placementFlags="10" centroidInside="1" offsetUnits="MM" centroidWhole="0" maxCurvedCharAngleIn="25" maxCurvedCharAngleOut="-25" repeatDistance="0"/>
      <rendering obstacleType="0" upsidedownLabels="0" mergeLines="0" scaleMax="2500" fontMaxPixelSize="10000" labelPerPart="1" obstacleFactor="1" displayAll="0" limitNumLabels="0" fontMinPixelSize="3" drawLabels="1" zIndex="0" minFeatureSize="0" maxNumLabels="2000" obstacle="1" scaleVisibility="1" fontLimitPixelSize="0" scaleMin="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option name="properties"/>
          <Option type="QString" name="type" value="collection"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory labelPlacementMethod="XHeight" lineSizeType="MM" backgroundColor="#ffffff" enabled="0" maxScaleDenominator="1e+8" rotationOffset="270" minScaleDenominator="0" penAlpha="255" scaleDependency="Area" height="15" width="15" sizeScale="3x:0,0,0,0,0,0" penColor="#000000" scaleBasedVisibility="0" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" penWidth="0" minimumSize="0" opacity="1" diagramOrientation="Up" barWidth="5" backgroundAlpha="255">
      <fontProperties style="" description="Cantarell,11,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" priority="0" obstacle="0" showAll="1" linePlacementFlags="18" zIndex="0" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="KKOD">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="KATEGORI">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="fid" index="0"/>
    <alias name="" field="KKOD" index="1"/>
    <alias name="" field="KATEGORI" index="2"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="fid" expression=""/>
    <default applyOnUpdate="0" field="KKOD" expression=""/>
    <default applyOnUpdate="0" field="KATEGORI" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" exp_strength="0" constraints="3" notnull_strength="1" field="fid"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0" field="KKOD"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" notnull_strength="0" field="KATEGORI"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="fid" desc=""/>
    <constraint exp="" field="KKOD" desc=""/>
    <constraint exp="" field="KATEGORI" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column hidden="0" type="field" name="fid" width="-1"/>
      <column hidden="0" type="field" name="KKOD" width="-1"/>
      <column hidden="0" type="field" name="KATEGORI" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS formulär kan ha en Pythonfunktion som anropas när formuläret öppnas.

Använd denna funktion för att lägga till extra logik till dina formulär.

Skriv in namnet på funktionen i fältet "Python Init function".
Ett exempel nedan:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="KATEGORI" editable="1"/>
    <field name="KKOD" editable="1"/>
    <field name="fid" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="KATEGORI"/>
    <field labelOnTop="0" name="KKOD"/>
    <field labelOnTop="0" name="fid"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip>id</mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
