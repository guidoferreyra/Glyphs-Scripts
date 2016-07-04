#MenuTitle: Copy Anchors from base glyph
# -*- coding: utf-8 -*-
__doc__="""
On a suffixed glyph run the script to copy the anchors from the default version. (i.e. run on /a.ss01 and get /a anchors).
"""
from Foundation import NSPoint

font = Glyphs.font

selectedLayers = font.selectedLayers

def	copyAnchor(thisLayer, anchorName, anchorX, anchorY):
	newAnchor = GSAnchor.alloc().init()
	newAnchor.name = anchorName
	thisLayer.addAnchor_( newAnchor )
	newPosition = NSPoint( anchorX, anchorY)
	newAnchor.setPosition_( newPosition )	


for thisLayer in selectedLayers:
	glyphName = thisLayer.parent.name
	
	id = thisLayer.layerId
	
	baseName = glyphName[0:glyphName.find('.')]

	for anchor in font.glyphs[baseName].layers[id].anchors:
		anchorName = anchor.name
		anchorX = anchor.position.x
		anchorY = anchor.position.y
		
		copyAnchor(thisLayer, anchorName, anchorX, anchorY)		