#MenuTitle: New Tab with not monospaced glyphs
# -*- coding: utf-8 -*-
__doc__="""
(UI) Opens a newtab with those glyphs that doesn’t match with the indicated glyph width. Useful for checking monospaced fonts or tabular glyphs.
"""

from GlyphsApp import *
from vanilla import *

font = Glyphs.font

class notMono(object):

	def __init__(self):
		
		
		monoW = 600
		self.w = FloatingWindow((160, 70), "Check Width")
		self.w.textBox = EditText((10, 10, 60, 20), monoW)
		self.w.EditText = TextBox((80, 10, 90, 20), "upm")
		self.w.button = Button((10, 40, -10, 20), "Check & Open",
							callback=self.buttonCallback)
		self.w.open()

	def buttonCallback(self, sender):
		selectedLayers = font.selectedLayers
		customWidth = self.w.textBox.get()
		notMonoList = []
		for layer in selectedLayers:
			if layer.width != float(customWidth):
				print (layer.parent.name, layer.name, layer.width)
				notMonoList.append(layer.parent.name)

		tabString =  "/%s" % "/".join(notMonoList) 

		font.newTab( tabString )

notMono()




