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

#Dictionary of anchors for Lowercase
lowerDict = {
"a":("bottom", "top", "grave", "acute", "ogonek",),
"c":("bottom", "cedilla", "top", "acute",),
"d":("bottom", "topRight", "top",),
"e":("bottom", "ogonek", "top", "grave", "acute",),
"g":("acute", "bottom", "top",),
"h":("bottom", "top",),
"i":("bottom", "ogonek",),
"idotless":("acute", "grave", "top",),
"jdotless":("top",),
"k":("bottom",),
"l":("bottom", "center", "topRight", "acute",),
"n":("acute", "bottom", "top", "topLeft",),
"o":("bottom", "ogonek", "grave", "top", "acute",),
"r":("acute", "bottom", "top",),
"s":("bottom", "cedilla", "top", "acute",),
"t":("cedilla", "topRight", "bottom",),
"u":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute",),
"w":("top", "grave", "acute",),
"y":("top", "grave", "acute",),
"z":("acute", "bottom", "top",),
"ae":("acute",),
"s_t":( "bottomRight", "bottomLeft", "cedilla", "topRight",),
"c_t":( "cedilla", "bottom", "topRight",),
"acute":("_acuteHigh", "_acute",),
"apostrophemod":("_topLeft",),
"breve":("_top",),
"breveinvertedcomb":("_top",),
"caron":("_topHigh", "_top",),
"caron.alt":("_topRight",),
"cedilla":("_cedilla",),
"circumflex":("_top",),
"commaaccentcomb":("_bottom", "_bottomLeft", "_bottomRight",),
"dblgravecomb":("_top",),
"dieresis":("_top",),
"dotaccent":("_top",),
"dotbelowcomb":("_bottom",),
"grave":("_graveHigh", "_grave",),
"hungarumlaut":("_top",),
"kreska":("_top",),
"macron":("_topHigh", "_top",),
"ogonek":("_ogonek",),
"ring":("_top",),
"tilde":("_top",),
}
#Dictionary of anchors for Uppercase
upperDict = {
"A":("bottom", "ogonek", "top", "grave", "acute",),
"C":("bottom", "cedilla", "top", "acute",),
"D":("top", "bottom",),
"E":("bottom", "ogonek", "top", "grave", "acute",),
"G":("acute", "bottom", "top",),
"H":("top", "bottom",),
"I":("bottom", "ogonek", "top", "grave", "acute",),
"J":("top",),
"K":("bottom",),
"L":("bottom", "center", "topRight", "acute",),
"N":("acute", "bottom", "top",),
"O":("bottom", "ogonek", "top", "grave", "acute",),
"R":("acute", "bottom", "top",),
"S":("bottom", "cedilla", "top", "acute",),
"T":("cedilla", "bottom", "top",),
"U":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute",),
"W":("acute", "grave", "top",),
"Y":("acute", "grave", "top",),
"Z":("acute", "bottom", "top",),
"AE":("acute",),
"acute.case":("_acuteHigh", "_acute",),
"breve.case":("_top",),
"breveinvertedcomb.case":("_top",),
"caron.case":("_topHigh", "_top",),
"cedilla.case":("_cedilla",),
"circumflex.case":("_top",),
"commaaccentcomb.case":("_bottom",),
"dblgravecomb.case":("_top",),
"dieresis.case":("_top",),
"dotaccent.case":("_top",),
"dotbelowcomb.case":("_bottom",),
"grave.case":("_graveHigh", "_grave",),
"hungarumlaut.case":("_top",),
"kreska.case":("_top",),
"macron.case":("_topHigh", "_top",),
"ogonek.case":("_ogonek",),
"ring.case":("_top",),
"tilde.case":("_top",),
}

#Dictionary of anchors for SmallCaps
smallDict = {
"a.sc":("bottom", "ogonek", "top", "grave", "acute",),
"c.sc":("bottom", "cedilla", "top", "acute",),
"d.sc":("top", "bottom",),
"e.sc":("bottom", "ogonek", "top", "grave", "acute",),
"g.sc":("acute", "bottom", "top",),
"h.sc":("top", "bottom",),
"i.sc":("bottom", "ogonek", "top", "grave", "acute",),
"j.sc":("top",),
"k.sc":("bottom",),
"l.sc":("bottom", "center", "topRight", "acute",),
"n.sc":("acute", "bottom", "top", "topLeft",),
"o.sc":("bottom", "ogonek", "top", "grave", "acute",),
"r.sc":("acute", "bottom", "top",),
"s.sc":("bottom", "cedilla", "top", "acute",),
"t.sc":("cedilla", "bottom", "top",),
"u.sc":("bottom", "acuteHigh", "graveHigh", "grave", "ogonek", "topHigh", "top", "acute",),
"w.sc":("acute", "grave", "top",),
"y.sc":("acute", "grave", "top",),
"z.sc":("acute", "bottom", "top",),
"ae.sc":("acute",),
"acute.sc":("_acuteHigh", "_acute",),
"apostrophemod.sc":("_topLeft",),
"breve.sc":("_top",),
"breveinvertedcomb.sc":("_top",),
"caron.sc":("_topHigh", "_top",),
"cedilla.sc":("_cedilla",),
"circumflex.sc":("_top",),
"commaaccentcomb.sc":("_bottom", "_bottomLeft", "_bottomRight",),
"dblgravecomb.sc":("_top",),
"dieresis.sc":("_top",),
"dotaccent.sc":("_top",),
"dotbelowcomb.sc":("_bottom",),
"grave.sc":("_graveHigh", "_grave",),
"hungarumlaut.sc":("_top",),
"kreska.sc":("_top",),
"macron.sc":("_topHigh", "_top",),
"ogonek.sc":("_ogonek",),
"ring.sc":("_top",),
"tilde.sc":("_top",),
}

	

def selectDict(glyphName, gDict, gPosDict, gLayer):
    for anchorName in gDict[glyphName]:
        if anchorName in gPosDict:
            posXY = gPosDict[anchorName]
        else:
            posXY = (100, 200)
        pos = NSPoint(posXY[0], posXY[1])
        addAnchorToLayer(gLayer, anchorName, pos)

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
lowerGlyphNames = lowerDict.keys() 
upperGlyphNames = upperDict.keys()
smallGlyphNames = smallDict.keys()


def angle(angle, height, yPos):
	'''
	Italic Angle
	'''
	# Thank to Mark Frömberg for this
	offset = math.tan(math.radians(angle)) * height / 2
	shift = math.tan(math.radians(angle)) * yPos - offset
	
	return shift


# iterate through all layers of all selected glyphs:
for thisGlyph in allSelectedGlyphs:
	for thisLayer in thisGlyph.layers:
		thisLayer.setAnchors_( None )
		# determine the master to which the layer belongs:
		masterID = thisLayer.associatedMasterId
		thisMasterXheight = font.masters[masterID].xHeight
		thisMasterUpperheight = font.masters[masterID].capHeight
		thisMasterSmallheight = float(font.masters[masterID].customParameters['smallCapHeight'])
		thisMasterAngle = thisLayer.glyphMetrics()[5]


		
		#Dictionaries whith the anchors positions. 
		lowerPosDict = {
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
			"_acute":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_bottom":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterXheight, 0), 0),
			"_center":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_grave":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_ogonek":(thisLayer.bounds.size.width, 0),
			"_top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_acuteHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_graveHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
			"_topRight":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterXheight, thisMasterXheight), thisMasterXheight),
		}

		upperPosDict = {
			"acute":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"bottom":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterUpperheight, 0), 0),
			"center":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight/2), thisMasterUpperheight/2),
			"grave":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"ogonek":(thisLayer.bounds.size.width, 0),
			"top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight+100), thisMasterUpperheight+100),
			"acuteHigh":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight+100), thisMasterUpperheight+100),
			"graveHigh":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight+100), thisMasterUpperheight+100),
			"topRight":(thisLayer.bounds.size.width, thisMasterUpperheight),
			"_acute":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_bottom":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterUpperheight, 0), 0),
			"_center":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_grave":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_ogonek":(thisLayer.bounds.size.width, 0),
			"_top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_acuteHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_graveHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
			"_topRight":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterUpperheight, thisMasterUpperheight), thisMasterUpperheight),
		}
		smallPosDict = {
			"acute":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"bottom":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterSmallheight, 0), 0),
			"center":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight/2), thisMasterSmallheight/2),
			"grave":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"ogonek":(thisLayer.bounds.size.width, 0),
			"top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight+100), thisMasterSmallheight+100),
			"acuteHigh":(thisLayer.width/2 - 20+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight+100), thisMasterSmallheight+100),
			"graveHigh":(thisLayer.width/2 + 20+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight+100), thisMasterSmallheight+100),
			"topRight":(thisLayer.bounds.size.width, thisMasterSmallheight),
			"_acute":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_bottom":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterSmallheight, 0), 0),
			"_center":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_grave":(thisLayer.width/2+ angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_ogonek":(thisLayer.bounds.size.width, 0),
			"_top":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_topHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_acuteHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_graveHigh":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
			"_topRight":(thisLayer.width/2 + angle(thisMasterAngle, thisMasterSmallheight, thisMasterSmallheight), thisMasterSmallheight),
		}

		# determine the master to which the layer belongs:
		thisGlyphName = thisGlyph.name
		# if it is listed in anchorDict, add the anchor at the given position:
		if thisGlyphName in lowerGlyphNames:
 		   selectDict(thisGlyphName, lowerDict, lowerPosDict, thisLayer)

		elif thisGlyphName in upperGlyphNames:
		    selectDict(thisGlyphName, upperDict, upperPosDict, thisLayer)
		 
		elif thisGlyphName in smallGlyphNames:
		    selectDict(thisGlyphName, smallDict, smallPosDict, thisLayer)

		else:
		    print "the /" + thisGlyphName + " glyph is not in the dictionary"
