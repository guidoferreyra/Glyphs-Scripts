#MenuTitle: Slant Anchors
# -*- coding: utf-8 -*-
__doc__="""
Displace anchors according to master italic angle
"""

import GlyphsApp
from Foundation import NSPoint
import math

font = Glyphs.font
selectedLayers = font.selectedLayers


def angle(angle, height, yPos):
    offset = math.tan(math.radians(angle)) * height / 2
    shift = math.tan(math.radians(angle)) * yPos - offset
    return shift


for thisLayer in selectedLayers:
#Set variables
    masterID = thisLayer.associatedMasterId
    print masterID
    thisMasterXheight = font.masters[masterID].xHeight
    thisMasterAngle = thisLayer.glyphMetrics()[5]

    for thisAnchor in thisLayer.anchors:
        posY = thisAnchor.position.y
        newPosition =  thisAnchor.position.x + angle(thisMasterAngle, thisMasterXheight, posY)
        print newPosition, thisAnchor
        thisAnchor.position = NSPoint(newPosition, posY)  

