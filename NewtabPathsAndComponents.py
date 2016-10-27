#MenuTitle: Newtab with components and paths
# -*- coding: utf-8 -*-
__doc__="""
Open in a new tab glyphs that contains components and paths.
"""

import GlyphsApp

Glyphs.clearLog()
Glyphs.showMacroWindow()
thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers



lista = []
def process (thisLayer):
	if len( thisLayer.components ) > 0 and len( thisLayer.paths ):
		lista.append(thisGlyph.name)
		tabString = "/%s" % "/".join(thisLayer.parent.name)


for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	process (thisLayer)

tabString =  "/%s" % "/".join(lista) 
thisFont.newTab( tabString )
