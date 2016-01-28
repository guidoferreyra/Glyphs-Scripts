#MenuTitle: Anchor Backup and Clone
# -*- coding: utf-8 -*-
__doc__="""
(UI) Backup anchors and copy layer to layer.
"""

from GlyphsApp import *
from vanilla import *
from Foundation import NSPoint


font = Glyphs.font


class AnchorTeleporter(object):

	def __init__(self):
		
		self.createLayerList()
		infoText = ""
		self.w = Window((240, 180), "Anchor Backup and Clone")
		self.w.button = Button((10, 10, -10, 20), "Backup Anchors",
							callback=self.buttonCallback)
		self.w.line = HorizontalLine((10, 40, -10, 1))
		self.w.textBox = TextBox((10, 50, -10, 17), "Clone Anchors from")
		self.w.popUpButton = PopUpButton((10, 75, -50, 20),
							  self.createLayerList())
		self.w.reloadButton = Button((-40, 75, -10, 20), u"↺",
							callback=self.reloadButtonCallback)
		self.w.restoreButton = Button((10, 105, -10, 20), "Clone Anchors", callback=self.cloneCallback)
		self.w.line2 = HorizontalLine((10, 135, -10, 1))
		self.w.box = Box((10, 145, -10, 24))
		self.w.box.infoBox = TextBox((0, 0, -0, -0), infoText, alignment='center', sizeStyle='small')

		self.w.open()

	def buttonCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		self.w.box.infoBox.set("Anchors Backuped")
		def createLayer (thisLayer):
			glyph = thisLayer.parent
			newLayer = GSLayer()
			#print font.masters[masterId]
			thisMaster = font.masters[thisLayer.associatedMasterId]
			newLayer.associatedMasterId = thisMaster.id

			font.glyphs[glyph.name].layers.append(newLayer)
			id = newLayer.layerId
			backupLayer = font.glyphs[thisLayer.parent.name].layers[id]
			relatedMaster =  font.masters[backupLayer.associatedMasterId].name
			newLayer.name = 'AnchorBackup ' + str(relatedMaster)

			return backupLayer

		#Copy anchors to backup layer
		def copyToBackup(backupLayer, anchorName, x, y):
			newAnchor = GSAnchor.alloc().init()
			newAnchor.name = anchorName
			backupLayer.addAnchor_( newAnchor )
			newPosition = NSPoint( x, y)
			newAnchor.setPosition_( newPosition )

		for thisLayer in selectedLayers:
			backupLayer = createLayer (thisLayer)
			allAnchors = thisLayer.anchors
			for thisAnchor in allAnchors:
				anchorName = thisAnchor.name
				x = thisAnchor.position.x
				y = thisAnchor.position.y
	
				copyToBackup (backupLayer, anchorName, x, y)
				# Reload List
				layerList = self.createLayerList()
				self.w.popUpButton.setItems( layerList )

	def createLayerList(self):
		selectedLayers = Glyphs.font.selectedLayers
		
		for thisLayer in selectedLayers:
			layerList = []
			glyph = thisLayer.parent
			for layer in glyph.layers:
				layerList.append(layer.name)
			return layerList

	def reloadButtonCallback( self, sender ):
		layerList = self.createLayerList()
		self.w.popUpButton.setItems( layerList )
		self.w.box.infoBox.set("Anchor list reloaded")

	def cloneCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		self.w.box.infoBox.set("Anchors cloned!")
		
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
		
			for i in font.glyphs[glyph.name].layers:
				if i.name == popchoose [layerIndex]:
					backupLayer = i

			allAnchors = backupLayer.anchors
			
			for thisAnchor in allAnchors:
				anchorName = thisAnchor.name
				x = thisAnchor.position.x
				y = thisAnchor.position.y
	
				copyToFront (thisLayer, anchorName, x, y)

AnchorTeleporter()