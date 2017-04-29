#MenuTitle: Import Anchors
# -*- coding: utf-8 -*-
__doc__="""
(UI) Import anchors from antother font.
"""

from GlyphsApp import *
from vanilla import *
from Foundation import NSPoint


font = Glyphs.font


class AnchorTeleporter(object):

	def __init__(self):
		infoText = ""
		self.w = FloatingWindow((240, 190), "Import Anchors")
		self.w.textBox = TextBox((10, 10, -10, 17), "Import Anchors from")
		self.w.popUpFont = PopUpButton((10, 35, -10, 20),
							  self.createFontList(),
                              callback=self.popUpButtonCallback)
		self.w.textBox2 = TextBox((10, 65, -10, 17), "Layer:")		
		self.w.popUpButton = PopUpButton((10, 85, -10, 20),[""])
		self.w.restoreButton = Button((10, 115, -10, 20), "Copy Anchors", callback=self.cloneCallback)
		self.w.line2 = HorizontalLine((10, 145, -10, 1))
		self.w.box = Box((10, 155, -10, 24))
		self.w.box.infoBox = TextBox((0, 0, -10, -0), infoText, alignment='center', sizeStyle='small')
		self.w.popUpButton.enable( False )
		self.w.restoreButton.enable( False )
		self.w.open()

	def popUpButtonCallback(self, sender):
		selectedFont = Glyphs.fonts[sender.get()]
		selectedLayers = selectedFont.selectedLayers
		for thisLayer in selectedLayers:
			layerList = []
			glyph = thisLayer.parent
			for layer in glyph.layers:
				layerList.append(layer.name)
			self.w.popUpButton.setItems( layerList )
			self.w.popUpButton.enable( True )
			self.w.restoreButton.enable( True )

	def createFontList(self):
		fonts = Glyphs.fonts
		fontList = []
		for thisFont in fonts:
			fontList.append(thisFont.familyName)
		return fontList

	def reloadButtonCallback( self, sender ):
		layerList = self.createLayerList()
		self.w.popUpButton.setItems( layerList )
		self.w.box.infoBox.set("Anchor list reloaded")

	def cloneCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		self.w.box.infoBox.set("Anchors Copied!")
		
		def copyToFront( thisLayer, anchorName, x, y):
			newAnchor = GSAnchor.alloc().init()
			newAnchor.name = anchorName
			thisLayer.addAnchor_( newAnchor )
			newPosition = NSPoint( x, y)
			newAnchor.setPosition_( newPosition )

		for thisLayer in selectedLayers:
			glyph = thisLayer.parent
			layerIndex = self.w.popUpButton.get()
			popchoose = self.w.popUpButton.getItems()
			
			
			try:
			
				for i in Glyphs.fonts[1].glyphs[glyph.name].layers:
			
					if i.name == list(popchoose) [layerIndex]:
						backupLayer = i
						break

				allAnchors = backupLayer.anchors
				
				for thisAnchor in allAnchors:
					anchorName = thisAnchor.name
					x = thisAnchor.position.x
					y = thisAnchor.position.y
		
					copyToFront (thisLayer, anchorName, x, y)
			except:
				pass

AnchorTeleporter()