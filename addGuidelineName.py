#MenuTitle: Add name to Guideline
# -*- coding: utf-8 -*-
__doc__="""
(UI) Add name to guideline.
"""

from GlyphsApp import *
from vanilla import *


class addGuidelineName(object):

	if len(Layer.selection) == 1 and type(Layer.selection[0]) == GSGuideLine:
		def __init__(self):
		
			self.w = FloatingWindow((250, 70), "Add Name to Guideline")
			self.w.label = TextBox((10, 10, -120, 20), "Guideline Name:")
			self.w.textInName = EditText((-130, 10, -10, 20), "", sizeStyle='small')
			self.w.createButton = Button((10, -30, -10, 20), "Add Name", callback=self.buttonCallback)
		
			self.w.open()

		def buttonCallback(self, sender):
			Layer.selection[0].name = self.w.textInName.get()
			Glyphs.redraw()
			
	else:
			Message("Add name to guideline", "Please select a guideline before", OKButton=None)	


addGuidelineName()