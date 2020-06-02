#MenuTitle: Add name to Guideline
# -*- coding: utf-8 -*-
__doc__="""
(UI) Add name to guideline.
"""

from GlyphsApp import *
from vanilla import *


class addGuidelineName(object):

	def __init__(self):
		self.w = FloatingWindow((250, 70), "Add Name to Guideline")
		self.w.label = TextBox((10, 10, -120, 20), "Guideline Name:")
		self.w.textInName = EditText((-130, 10, -10, 20), "", sizeStyle='small')
		self.w.createButton = Button((10, -30, -10, 20), "Add Name", callback=self.buttonCallback)
		self.w.open()

	def buttonCallback(self, sender):
		guidesToName = []
		for selection in Layer.selection:
			if isinstance(selection, GSGuideLine):
				guidesToName.append(selection)
		
		if len(guidesToName) > 0:
			for guide in guidesToName:
				guide.name = self.w.textInName.get()
			Glyphs.redraw()
		else:
			Message("Please select at least one guideline", "Add name to guideline")

addGuidelineName()
