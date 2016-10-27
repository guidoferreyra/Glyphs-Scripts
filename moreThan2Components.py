#MenuTitle: New tab with more than 2 components
# -*- coding: utf-8 -*-
__doc__="""
Open in a new tab the glyphs with more than two components
"""

import GlyphsApp

Glyphs.clearLog()
Glyphs.showMacroWindow()
thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers



lista = []
def process (thisLayer):
	if len( thisLayer.components ) > 2:
		lista.append(thisGlyph.name)
		tabString = "/%s" % "/".join(thisLayer.parent.name)


for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	process (thisLayer)

tabString =  "/%s" % "/".join(lista) 
thisFont.newTab( tabString )
