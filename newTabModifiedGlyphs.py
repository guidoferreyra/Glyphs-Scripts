#MenuTitle: New tab with modified glyphs
# -*- coding: utf-8 -*-
__doc__="""
(UI) Opens in a new tab modified glyphs after or before certain date.
"""

from GlyphsApp import *
from vanilla import *

import time
import datetime

glyphList = []
thisFont = Glyphs.font


class openGlyphs(object):

	def __init__(self):
		
		self.w = Window((240, 115), "New tab with modified glyphs")		
		self.w.radioGroup = RadioGroup((10, 10, 140, 40),
                                ["After", "Before"], isVertical=False)
		self.w.fechaPick = DatePicker((10, 50, -10, 22), timeDisplay=None)
		self.w.goButton = Button((10, -30, -10, 20), "Open in a new tab", callback=self.buttonCallback)
		self.w.radioGroup.set(0)
		self.w.open()


	


	def buttonCallback(self, sender):
		Glyphs.showMacroWindow()
		Glyphs.clearLog()
		pickedDate = self.w.fechaPick.get()
		split1 = str(pickedDate).split(' ')[0]
		split2 = split1.split('-')
		year = int(split2[0])
		month = int(split2[1])
		day = int(split2[2])
		date = datetime.date(year,month,day)
		unixtime = time.mktime(date.timetuple())

		optionChoice = self.w.radioGroup.get()
		## #sortedglyphList = sorted(glyphList, key=lambda x: x[1])
		for glyph in Font.glyphs:	
			if optionChoice == 0:
		 		if glyph.lastChange > unixtime:
		 			glyphList.append(glyph.name)
		 	else:
		 		if glyph.lastChange < unixtime:
		 			glyphList.append(glyph.name)

		
		tabString =  "/%s" % "/".join(glyphList) 
		thisFont.newTab( tabString )
		for glyph in glyphList:
			thisGlyph = thisFont.glyphs[glyph]
			lastChange = time.strftime("%d/%m/%y", time.localtime(thisGlyph.lastChange))
			print thisGlyph.name+": "+lastChange

openGlyphs()
