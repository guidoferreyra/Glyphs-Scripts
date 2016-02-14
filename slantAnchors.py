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
        
        self.w = Window((160, 100), "Check Nodes")
        self.w.textBox = EditText((10, 10, 60, 20), "")
        self.w.EditText = TextBox((80, 10, 90, 20), u"\u00B0")
        self.w.checkBox = CheckBox((10, 40, -10, 20), "Use italic angle",
                           callback=self.checkBoxCallback, value=False)
       	self.w.button = Button((10, 70, -10, 20), "Move",
                            callback=self.buttonCallback)
        self.w.open()

    def checkBoxCallback(self, sender):
        print "check box state change!", sender.get()


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
               	
               	if self.w.checkBox.get() == True:
                	newPosition =  thisAnchor.position.x + angle(thisMasterAngle, thisMasterXheight, posY)
                	thisAnchor.position = NSPoint(newPosition, posY)
                else:
                	customAngle = self.w.textBox.get()

                	newPosition =  thisAnchor.position.x + angle(float(customAngle), thisMasterXheight, posY)
                	thisAnchor.position = NSPoint(newPosition, posY)

slantAnchor()

