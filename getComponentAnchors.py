#MenuTitle: Get component anchors
# -*- coding: utf-8 -*-
__doc__="""
In a glyph made of components, gets component acnhors and add it to the current layer, useful for ligatures made of components.
"""

font = Glyphs.font
i = 1
for thisLayer in font.selectedLayers:
	thisLayerID = thisLayer.associatedMasterId
	for thisComponent in thisLayer.components:
		offsetX =  thisComponent.position.x
		offsetY = thisComponent.position.y
		referenceGlyph = font.glyphs[thisComponent.componentName]
		
		for referenceAnchor in referenceGlyph.layers[thisLayerID].anchors:
			
			newAnchor = GSAnchor.alloc().init()
			newAnchor.name = referenceAnchor.name + "_" + str(i)
			thisLayer.addAnchor_( newAnchor )
			newPosition = NSPoint( referenceAnchor.x + offsetX, referenceAnchor.y + offsetY)
			newAnchor.setPosition_( newPosition )
		i+= 1
			
