#MenuTitle: CenterAnchors
# -*- coding: utf-8 -*-
__doc__="""
This script center all anchors of all layers
"""
import GlyphsApp
from Foundation import NSPoint
import math

font = Glyphs.font
allSelectedGlyphs = [l.parent for l in font.selectedLayers]
print allSelectedGlyphs
master = font.masters[0]
glyph = thisLayer.parent


def angle(angle, height, yPos):
    offset = math.tan(math.radians(angle)) * height / 2
    shift = math.tan(math.radians(angle)) * yPos - offset
    return shift


for thisGlyph in allSelectedGlyphs:

    for thisLayer in thisGlyph.layers:
    #Set variables
        masterID = thisLayer.associatedMasterId
        print masterID
        thisMasterXheight = font.masters[masterID].xHeight
        thisMasterAngle = thisLayer.glyphMetrics()[5]
        width = thisLayer.width

        for thisAnchor in thisLayer.anchors:
            posY = thisLayer.anchors[thisAnchor.name].position.y
            centerOfLayer = width/2 + angle(thisMasterAngle, thisMasterXheight, posY)

            thisLayer.anchors[thisAnchor.name].position = NSPoint(centerOfLayer, posY)  
