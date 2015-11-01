#MenuTitle: Add anchors to selected glyphs
# -*- coding: utf-8 -*-
__doc__="""
Using a dictionary the script adds anchors to all the master of the selected glyphs.
For those glyphs that are not in the dictionary the script do nothing.
Feel free to edit the dictionary to your needs.
There is also another dictionary with the position of the anchors. 
"""
#THIS SCRIPT is heavly based on Ohbendy's Place anchors in all masters
#https://github.com/ohbendy/Python-scripts-for-Glyphs
#Thanks to Mark Frömberg (mirque.de) for the angle function.

import GlyphsApp
from Foundation import NSPoint
import math
#Dictionary of anchors for each letter
anchorDict = {
#Minusculas
"a":("bottom", "top", "grave", "acute", "ogonek"),
"c":("bottom", "cedilla", "top", "acute"),
"d":("bottom", "topRight", "top"),
"e":("bottom", "ogonek", "top", "grave", "acute"),
"g":("acute", "bottom", "top"),
"h":("bottom", "top"),
"i":("bottom", "ogonek"),
"idotless":("acute", "grave", "top"),
"jdotless":("top"),
"k":("bottom"),
"l":("bottom", "center", "topRight", "acute"),
"n":("acute", "bottom", "top", "topLeft"),
"o":("bottom", "ogonek", "grave", "top", "acute"),
"r":("acute", "bottom", "top"),
"s":("bottom", "cedilla", "top", "acute"),
"t":("cedilla", "topRight", "bottom"),
"u":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute"),
"w":("top", "grave", "acute"),
"y":("top", "grave", "acute"),
"z":("acute", "bottom", "top"),
"ae":("acute"),
"s_t":( "bottomRight", "bottomLeft", "cedilla", "topRight",),
"c_t":( "cedilla", "bottom", "topRight",),
#Mayusculas
"A":("bottom", "ogonek", "top", "grave", "acute"),
"C":("bottom", "cedilla", "top", "acute"),
"D":("top", "bottom"),
"E":("bottom", "ogonek", "top", "grave", "acute"),
"G":("acute", "bottom", "top"),
"H":("top", "bottom"),
"I":("bottom", "ogonek", "top", "grave", "acute"),
"J":("top",),
"K":("bottom"),
"L":("bottom", "center", "topRight", "acute"),
"N":("acute", "bottom", "top"),
"O":("bottom", "ogonek", "top", "grave", "acute"),
"R":("acute", "bottom", "top"),
"S":("bottom", "cedilla", "top", "acute"),
"T":("cedilla", "bottom", "top"),
"U":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute"),
"W":("acute", "grave", "top"),
"Y":("acute", "grave", "top"),
"Z":("acute", "bottom", "top"),
"AE":("acute"),
#Versalitas
"a.sc":("bottom", "ogonek", "top", "grave", "acute"),
"c.sc":("bottom", "cedilla", "top", "acute"),
"d.sc":("top", "bottom"),
"e.sc":("bottom", "ogonek", "top", "grave", "acute"),
"g.sc":("acute", "bottom", "top"),
"h.sc":("top", "bottom"),
"i.sc":("bottom", "ogonek", "top", "grave", "acute"),
"j.sc":("top",),
"k.sc":("bottom"),
"l.sc":("bottom", "center", "topRight", "acute"),
"n.sc":("acute", "bottom", "top", "topLeft"),
"o.sc":("bottom", "ogonek", "top", "grave", "acute"),
"r.sc":("acute", "bottom", "top"),
"s.sc":("bottom", "cedilla", "top", "acute"),
"t.sc":("cedilla", "bottom", "top"),
"u.sc":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute"),
"w.sc":("acute", "grave", "top"),
"y.sc":("acute", "grave", "top"),
"z.sc":("acute", "bottom", "top"),
"ae.sc":("acute"),
#Acentos
"acute":("_acuteHigh", "_acute"),
"acute.case":("_acuteHigh", "_acute"),
"acute.sc":("_acuteHigh", "_acute"),
"apostrophemod":("_topLeft"),
"apostrophemod.sc":("_topLeft"),
"breve":("_top"),
"breve.case":("_top"),
"breve.sc":("_top"),
"breveinvertedcomb":("_top"),
"breveinvertedcomb.case":("_top"),
"breveinvertedcomb.sc":("_top"),
"caron":("_topHigh", "_top"),
"caron.alt":("_topRight"),
"caron.case":("_topHigh", "_top"),
"caron.sc":("_topHigh", "_top"),
"cedilla":("_cedilla"),
"cedilla.case":("_cedilla"),
"cedilla.sc":("_cedilla"),
"circumflex":("_top"),
"circumflex.case":("_top"),
"circumflex.sc":("_top"),
"commaaccentcomb":("_bottom", "_bottomLeft", "_bottomRight"),
"commaaccentcomb.case":("_bottom"),
"commaaccentcomb.sc":("_bottom", "_bottomLeft", "_bottomRight"),
"dblgravecomb":("_top"),
"dblgravecomb.case":("_top"),
"dblgravecomb.sc":("_top"),
"dieresis":("_top"),
"dieresis.case":("_top"),
"dieresis.sc":("_top"),
"dotaccent":("_top"),
"dotaccent.case":("_top"),
"dotaccent.sc":("_top"),
"dotbelowcomb":("_bottom"),
"dotbelowcomb.case":("_bottom"),
"dotbelowcomb.sc":("_bottom"),
"grave":("_graveHigh", "_grave"),
"grave.case":("_graveHigh", "_grave"),
"grave.sc":("_graveHigh", "_grave"),
"hungarumlaut":("_top"),
"hungarumlaut.case":("_top"),
"hungarumlaut.sc":("_top"),
"kreska":("_top"),
"kreska.case":("_top"),
"kreska.sc":("_top"),
"macron":("_topHigh", "_top"),
"macron.case":("_topHigh", "_top"),
"macron.sc":("_topHigh", "_top"),
"ogonek":("_ogonek"),
"ogonek.case":("_ogonek"),
"ogonek.sc":("_ogonek"),
"ring":("_top"),
"ring.case":("_top"),
"ring.sc":("_top"),
"tilde":("_top"),
"tilde.case":("_top"),
"tilde.sc":("_top"),
}


def addAnchorToLayer( thisLayer, anchorName, thisPosition):
	if thisLayer:
		newAnchor = GSAnchor.alloc().init()
		newAnchor.name = anchorName
		thisLayer.addAnchor_( newAnchor )
		newPosition = NSPoint( thisPosition[0], thisPosition[1])
		newAnchor.setPosition_( newPosition )
		

font = Glyphs.font
layer = font.selectedLayers[0]
glyph = layer.parent
master = font.masters[0]

allSelectedGlyphs = [l.parent for l in font.selectedLayers]
allGlyphNames = anchorDict.keys() # master names listed in anchorDict

def angle(angle, xHeight, yPos):
	'''
	Italic Angle
	'''
	# Thank to Mark Frömberg for this
	offset = math.tan(math.radians(angle)) * xHeight / 2
	shift = math.tan(math.radians(angle)) * yPos - offset
	
	return shift


# iterate through all layers of all selected glyphs:
for thisGlyph in allSelectedGlyphs:
	for thisLayer in thisGlyph.layers:
		thisLayer.setAnchors_( None )
		# determine the master to which the layer belongs:
		masterID = thisLayer.associatedMasterId
		thisMasterXheight = font.masters[masterID].xHeight
		thisMasterAngle = thisLayer.glyphMetrics()[5]

		#Dictionary whith the anchor position. 
		
		posDict = {
			"acute":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"bottom":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterXheight, 0), 0),
			"center":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight/2), thisMasterXheight/2),
			"grave":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"ogonek":(thisLayer.bounds.size.width, 0),
			"top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight+100), thisMasterXheight+100),
			"acuteHigh":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight+100), thisMasterXheight+100),
			"graveHigh":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight+100), thisMasterXheight+100),
			"topRight":(thisLayer.bounds.size.width, thisMasterXheight),
		}

		allAnchorNames = posDict.keys()

		# determine the master to which the layer belongs:
		thisGlyphName = thisGlyph.name
		# if it is listed in anchorDict, add the anchor at the given position:
		if thisGlyphName in allGlyphNames:
			for anchorName in anchorDict[thisGlyphName]:
				if anchorName in allAnchorNames:
					thisPositionXY = posDict[anchorName]

				else:
					thisPositionXY = (100, 200)

				thisPosition = NSPoint( thisPositionXY[0], thisPositionXY[1] )
				addAnchorToLayer( thisLayer, anchorName, thisPosition)
