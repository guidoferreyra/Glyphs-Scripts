#MenuTitle: Nodes near Alignment zones
# -*- coding: utf-8 -*-
__doc__="""
(UI) The script searches for nodes near the alignment zones using an slider as a threshold in units.
"""
from vanilla import *

class nearAlignment(object):

	def __init__(self):

		self.w = Window((180, 70), "Check Nodes")
		self.w.slider = Slider((10, 10, -10, 23),
			tickMarkCount=10,
			value=0, minValue=0, maxValue=40,
			callback=self.sliderCallback)
		self.w.textBox = TextBox((10, 40, -10, 17))
		self.updateInfoText()
		self.w.open()
	
	def updateInfoText(self, umbral=0):
		infoText = "Threshold: %d u" % int(umbral)
		self.w.textBox.set(infoText)
	
	def sliderCallback(self, sender):
		umbral = int(self.w.slider.get())
		self.updateInfoText(umbral)

		def insertArrow(thisLayer, posX, posY, width=30):
			arrow = GSAnnotation()
			arrow.position = (posX, posY)
			arrow.type = CIRCLE
			arrow.width = width
			thisLayer.annotations.append(arrow)
			Glyphs.boolDefaults["showAnnotations"] = True

		def zoneList(master):
			zoneList = []
			for z in master.alignmentZones:
				zoneOrigin = int(z.position)
				zoneEnd = zoneOrigin + int(z.size)
				if zoneOrigin < zoneEnd:
					zoneList.append((zoneOrigin, zoneEnd))
				else:
					zoneList.append((zoneEnd, zoneOrigin))
			return zoneList

		def nextToZone(thisLayer, masterZones, pos, umbral):
			for thisZone in masterZones:
				zoneOrigin = thisZone[0]
				zoneEnd = thisZone[1]

				if pos >= zoneOrigin - umbral and pos < zoneOrigin:
					# just below the zone
					return True
				if pos > zoneEnd and pos <= zoneEnd + umbral:
					# just above the zone
					return True

		font = Glyphs.font
		selectedLayers = font.selectedLayers

		for thisLayer in selectedLayers:
			thisLayer.setAnnotations_(None)
			masterId = thisLayer.associatedMasterId
			master = font.masters[masterId]

			masterZones = zoneList(master)

			for thisPath in thisLayer.paths:
				for thisNode in thisPath.nodes:
					if thisNode.type != GSOFFCURVE:
						posY = thisNode.y
						posX = thisNode.x
						
						if nextToZone(thisLayer, masterZones, posY, umbral) is True:
							insertArrow (thisLayer, posX, posY)
							print ("A")

nearAlignment()