#MenuTitle: Copy Anchors to Background
# -*- coding: utf-8 -*-
__doc__="""
This script copy the anchors and paste it on the background.
"""
from Foundation import NSPoint

thisFont = Glyphs.font
selectedLayers = Glyphs.font.selectedLayers 
	
def copyToBg( thisLayer, anchorName, x, y):
	newAnchor = GSAnchor.alloc().init()
	newAnchor.name = anchorName
	thisLayer.background.addAnchor_( newAnchor )
	newPosition = NSPoint( x, y)
	newAnchor.setPosition_( newPosition )

for thisLayer in selectedLayers:
	allAnchors = thisLayer.anchors
	for thisAnchor in allAnchors:
		anchorName = thisAnchor.name
		x = thisAnchor.position.x
		y = thisAnchor.position.y
		
		copyToBg (thisLayer, anchorName, x, y)
