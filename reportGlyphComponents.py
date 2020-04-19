#MenuTitle: Report Glyph Components
# -*- coding: utf-8 -*-
__doc__="""
Prints in the console the components used on selecteds glyphs. 
"""
Glyphs.clearLog()
Glyphs.showMacroWindow()
currentLayer = Glyphs.font.selectedLayers[0]
print (font.familyName, currentLayer.name)

for thisLayer in Glyphs.font.selectedLayers:
	glyphComponents = []
	for i in thisLayer.components:
		glyphComponents.append(i.name)

	print (thisLayer.parent.name +": %s" % ", ".join(glyphComponents))
