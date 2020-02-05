#MenuTitle: Get from next font
# -*- coding: utf-8 -*-
__doc__="""
(UI) Import anchors from antother font.
"""

from GlyphsApp import *
from vanilla import *
from Foundation import NSPoint
import copy

font = Glyphs.font

class AnchorTeleporter(object):

	def __init__(self):
		infoText = ""
		self.w = FloatingWindow((300, 320), "Get from next font")
		self.w.textBox = TextBox((10, 10, -10, 17), "Get from")
		self.w.popUpFont = PopUpButton((10, 35, -10, 20),
							  self.createFontList(),
                              callback=self.popUpFontCallback)
		self.w.textBox2 = TextBox((10, 65, -10, 17), "Layer:")		
		self.w.popUpLayers = PopUpButton((10, 85, -10, 20),[""])
		
		

		self.w.checkBoxPaths = CheckBox((10, 120, -10, 20), "import paths", value=False)
		self.w.checkBoxComponents = CheckBox((10, 145, -10, 20), "import components", value=False)
		self.w.checkBoxSidebearings = CheckBox((10, 170, -10, 20), "import Sidebearings", value=False)
		self.w.checkBoxAnchors = CheckBox((10, 195, -10, 20), "import Anchors", value=False)

		self.w.importButton = Button((10, -70, -10, 20), "Import", callback=self.cloneCallback)
		self.w.line2 = HorizontalLine((10, -40, -10, 1))
		self.w.box = Box((10, -30, -10, 24))
		self.w.box.infoBox = TextBox((0, 0, -10, -0), infoText, alignment='center', sizeStyle='small')

		self.w.popUpLayers.enable( False )
		self.w.importButton.enable( False )
		self.w.open()

	def popUpFontCallback(self, sender):
		thisLayer = Glyphs.font.selectedLayers[0]
		selectedFont = Glyphs.fonts[sender.get()]
		glyphName = thisLayer.parent.name
		layerList = []
		
		for layer in selectedFont.glyphs[glyphName].layers:
			layerList.append(layer.name)

		self.w.popUpLayers.setItems( layerList )
		self.w.popUpLayers.enable( True )
		self.w.importButton.enable( True )

	def createFontList(self):
		fonts = Glyphs.fonts
		fontList = []
		for thisFont in fonts:
			fontList.append(thisFont.filepath.split("/")[-1])
		return fontList

	def cloneCallback(self, sender):
		selectedLayers = Glyphs.font.selectedLayers
		
		varImportPaths = self.w.checkBoxPaths.get()
		varImportComponents = self.w.checkBoxComponents.get()
		varImportSidebearings = self.w.checkBoxSidebearings.get()
		varImportAnchors = self.w.checkBoxAnchors.get()
		
		self.w.box.infoBox.set("Anchors Copied!")

		
		def importAnchors ( thisLayer, anchorName, x, y):
			thisLayer.anchors[anchorName] = GSAnchor()
			thisLayer.anchors[anchorName].position = NSPoint(x,y)
			# thisLayer.anchors.append( newAnchor )


		def importPaths ( thisLayer, nextPath):
			thisLayer.paths.append( nextPath )

		def importComponents ( thisLayer, nextComponent):
			thisLayer.components.append( nextComponent )		

		def importSidebearings ( thisLayer, nextPath):
			thisLayer.paths.append( nextPath )

		for thisLayer in selectedLayers:
			glyph = thisLayer.parent
			layerIndex = self.w.popUpLayers.get()
			popchoose = self.w.popUpLayers.getItems()

			nextFontIndex = self.w.popUpFont.get()
			
			
			
			try:
			
				for i in Glyphs.fonts[nextFontIndex].glyphs[glyph.name].layers:
					
					if i.name == list(popchoose) [layerIndex]:
						nextFontLayer = i
						
						if varImportAnchors == True:
							nextFontAnchors = nextFontLayer.anchors
							
							for nextAnchor in nextFontAnchors:
								thisAnchor = nextAnchor.copy()
								thisLayer.anchors[ str(thisAnchor.name) ] = thisAnchor
								#anchorName = nextAnchor.name
								# x = nextAnchor.position.x
								# y = nextAnchor.position.y
					
								# importAnchors  (thisLayer, anchorName, x, y)

						if varImportPaths == True:
							nextFontPaths = nextFontLayer.paths
							for nextPath in nextFontPaths:					
								importPaths  (thisLayer, nextPath)

						if varImportComponents == True:
							nextFontComponents = nextFontLayer.components
							for nextComponent in nextFontComponents:					
								importComponents  (thisLayer, nextComponent)					

						if varImportSidebearings == True:
							if nextFontLayer.leftMetricsKey != None:
								thisLayer.leftMetricsKey = nextFontLayer.leftMetricsKey 
							else:
								thisLayer.LSB = nextFontLayer.LSB

							if nextFontLayer.rightMetricsKey != None:
								thisLayer.rightMetricsKey = nextFontLayer.rightMetricsKey 
							else:
								thisLayer.RSB = nextFontLayer.RSB

							self.w.box.infoBox.set("Data imported!")
						break		

					
			except Exception, e:
						print e

				

AnchorTeleporter()