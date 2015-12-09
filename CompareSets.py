#MenuTitle: CompareSets
# -*- coding: utf-8 -*-
__doc__="""
(UI) Shows diffrences between glyph sets and allows to add glyphs to fonts.
"""

from GlyphsApp import *
from vanilla import *

font1 = Glyphs.fonts[0]
font2 = Glyphs.fonts[1]
styleName1 = font1.instances[0].name
styleName2 = font2.instances[0].name


class ListDemo(object):
	
	lista1 = []
	lista2 = []
	
	def __init__(self):

		self.createLists()
		DiffLists = (self.lista1, self.lista2)

		#User interface elements
		self.w = Window((330, 400),"Compare Sets", minSize=(330,400), maxSize=(330,1000))
		self.w.textBox = TextBox((10, 10, 150, 55), "Missing on \n" + font1.familyName + "\n" + styleName1)
		self.w.myList = List((10, 70, 150, -40), self.lista2)
		self.w.button = Button((10, -30, 150, 20), "Add to font",
							callback=self.button1Callback)
					 
		self.w.textBox2 = TextBox((170, 10, -10, 55), "Missing on \n" + font2.familyName + "\n" + styleName2)                     
		self.w.myList2 = List((170, 70, 150, -40), self.lista1)
		self.w.button2 = Button((170, -30, 150, 20), "Add to font",callback=self.button2Callback1)          
		self.w.open()

	#Button Callbacks
	def button1Callback(self, sender):
		seleccion = self.w.myList.getSelection()
		trash = []
		# Iterate over the selection, add glyph to font and append to trash list.
		for i in seleccion:
			name = self.w.myList.__getitem__(i)
			font1.glyphs.append(GSGlyph(name))
			trash.append(name)
			#Add automatic components to the created glyph.
			for master in font1.masters:
				layer = font1.glyphs[name].layers[master.id]
				layer.makeComponents()
		#Iterates over the trash list and remove the element from the UI list.
		for ii in trash:
			self.w.myList.remove(ii)	
			


	def button2Callback1(self, sender):
		seleccion = self.w.myList.getSelection()
		trash = []
		# Iterate over the selection, add glyph to font and append to trash list.
		for i in seleccion:
			name = self.w.myList2.__getitem__(i)
			font2.glyphs.append(GSGlyph(name))
			trash.append(name)
			#Add automatic components to the created glyph.
			for master in font2.masters:
				layer = font2.glyphs[name].layers[master.id]
				layer.makeComponents()
		#Iterates over the trash list and remove the element from the UI list.
		for ii in trash:
			self.w.myList.remove(ii)
	
	def createLists(self):
		# Create lists with the name of the glyphs of each font
		for a in font1.glyphs:
			self.lista1.append(a.name) #A, B, C, D, etc.
		for a in font2.glyphs:
			self.lista2.append(a.name)
		#Create sets of the lists for later comparision.
		font1Set = set(self.lista1)
		font2Set = set(self.lista2)
		#Create new sets with the differences.
		OneDiff = font1Set.difference(font2Set)
		TwoDiff = font2Set.difference(font1Set)
		#Transorm the sets in list again to send it to the UI
		self.lista1 = list(OneDiff)
		self.lista2 = list(TwoDiff)
		
# Glyphs.clearLog()
# Glyphs.showMacroWindow()
ListDemo()