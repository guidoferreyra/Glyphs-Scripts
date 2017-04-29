#MenuTitle: New tab with more than x components
# -*- coding: utf-8 -*-
__doc__="""
(UI) Opens in a new tab the glyphs with more than the indicated ammout of components
"""

import GlyphsApp


thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers


class newTabXComponents(object):

	def __init__(self):
		
		
		compAmount = 1
		self.w = FloatingWindow((250, 90), "Amount of components")
		self.w.EditText = TextBox((10, 10, 250, 20), "New tab with glyphs with")
		self.w.EditText2 = TextBox((10, 35, 90, 20), "more than")
		self.w.textBox = EditText((78, 35, 30, 20), compAmount)
		self.w.EditText3 = TextBox((110, 35, 90, 20), "components")
		self.w.button = Button((10, 60, -10, 20), "Check & Open",
							callback=self.buttonCallback)
		self.w.open()

	

	def buttonCallback(self, sender):

		lista = []
		
		amoutOfComponents = self.w.textBox.get()
		for thisLayer in selectedLayers:
			if len( thisLayer.components ) > int(amoutOfComponents):
				print thisLayer.components
				thisGlyph = thisLayer.parent
				lista.append(thisGlyph.name)

		if len(lista) > 0:
			tabString =  "/%s" % "/".join(lista)
			thisFont.newTab( tabString )
		else:
			Glyphs.clearLog()
			Glyphs.showMacroWindow()
			print "No glyphs with more than", amoutOfComponents, "components"
newTabXComponents()



