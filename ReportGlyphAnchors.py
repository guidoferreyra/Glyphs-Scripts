#MenuTitle: Report Glyph Anchors
# -*- coding: utf-8 -*-
__doc__="""
Print in the console the anchors used on selected Glyphs. 
"""
Glyphs.clearLog()
Glyphs.showMacroWindow()
currentLayer = Glyphs.font.selectedLayers[0]
print (font.familyName, currentLayer.name)

for thisLayer in Glyphs.font.selectedLayers:
	glyphAnchors = []
	for i in thisLayer.anchors:
		glyphAnchors.append(i.name)

	print (thisLayer.parent.name +": %s" % ", ".join(glyphAnchors))
