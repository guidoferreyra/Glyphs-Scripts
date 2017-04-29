#MenuTitle: deleteNotes
# -*- coding: utf-8 -*-
__doc__="""
This Script delete notes in selected glyphs
"""

Font = Glyphs.font
selectedLayers = Font.selectedLayers

for layer in selectedLayers:
	layer.setAnnotations_(None)
