#MenuTitle: Anchor Backup and Clone
# -*- coding: utf-8 -*-
__doc__="""
(UI) Backup anchors and copy layer to layer
"""

from GlyphsApp import *
from vanilla import *
from Foundation import NSPoint


font = Glyphs.font


class AnchorTeleporter(object):

	def __init__(self):
		
		self.createLayerList()

		self.w = Window((240, 140), "Anchor Backup and Clone")
		self.w.button = Button((10, 10, -10, 20), "Backup Anchors",
							callback=self.buttonCallback)
		self.w.line = HorizontalLine((10, 40, -10, 1))
		self.w.textBox = TextBox((10, 50, -10, 17), "Restore Anchors from")
		self.w.popUpButton = PopUpButton((10, 80, -50, 20),
							  self.createLayerList())
		self.w.reloadButton = Button((-40, 80, -10, 20), u"↺",
							callback=self.reloadButtonCallback)
		self.w.restoreButton = Button((10, 110, -10, 20), "Restore Anchors", callback=self.restoreCallback)
		self.w.open()

	def buttonCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		layer = font.selectedLayers[0]
		glyph = layer.parent
		
		def createLayer (thisLayer):
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
			print "Anchors Restored!"

	def createLayerList(self):
		selectedLayers = Glyphs.font.selectedLayers
		layer = font.selectedLayers[0]
		glyph = layer.parent

		layerList = []
		
		for layer in glyph.layers:
		    layerList.append(layer.name)
		return layerList

	def reloadButtonCallback( self, sender ):
		layerList = self.createLayerList()
		self.w.popUpButton.setItems( layerList )

	def restoreCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		layer = font.selectedLayers[0]
		glyph = layer.parent
		
		def copyToFront( layer, anchorName, x, y):
			newAnchor = GSAnchor.alloc().init()
			newAnchor.name = anchorName
			layer.addAnchor_( newAnchor )
			newPosition = NSPoint( x, y)
			newAnchor.setPosition_( newPosition )

		for layer in selectedLayers:
			layerIndex = self.w.popUpButton.get()
			backupLayer = font.glyphs[glyph.name].layers[layerIndex]
			allAnchors = backupLayer.anchors
			
			for thisAnchor in allAnchors:
				anchorName = thisAnchor.name
				x = thisAnchor.position.x
				y = thisAnchor.position.y
	
				copyToFront (layer, anchorName, x, y)
			print "Anchors Restored!"



AnchorTeleporter()