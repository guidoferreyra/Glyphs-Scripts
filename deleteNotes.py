#MenuTitle: deleteNotes
# -*- coding: utf-8 -*-
__doc__="""
This Script delete notes
"""

Font = Glyphs.font
selectedLayers = Font.selectedLayers

for layer in selectedLayers:
	layer.setAnnotations_(None)
