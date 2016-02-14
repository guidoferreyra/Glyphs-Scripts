#MenuTitle: Slant Anchors
# -*- coding: utf-8 -*-
__doc__="""
Displace anchors according to master italic angle
"""

import GlyphsApp
from Foundation import NSPoint
from vanilla import *
import math

font = Glyphs.font
selectedLayers = font.selectedLayers


class slantAnchor(object):

    def __init__(self):
        
        umbral = 0
        infoText = "Threshold: " + str(umbral)
        self.w = Window((180, 70), "Check Nodes")
        self.w.textBox = TextBox((10, 10, -10, 17), "A TextBox")
        self.w.button = Button((10, 10, -10, 20), "A Button",
                            callback=self.buttonCallback)
        self.w.textBox = TextBox((10, 40, -10, 17), infoText)
        self.w.open()

    def buttonCallback(self, sender):


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

    nearAlignment()

