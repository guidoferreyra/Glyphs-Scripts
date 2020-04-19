#MenuTitle: Nodes near Alignment zones
# -*- coding: utf-8 -*-
__doc__="""
(UI) The script searches for nodes near the alignment zones using an slider as a threshold in units.
"""
from vanilla import *
font = Glyphs.font
selectedLayers = font.selectedLayers


class nearAlignment(object):

	def __init__(self):
		
		umbral = 0
		infoText = "Threshold: "+ str(umbral) + " upm"
		self.w = Window((180, 70), "Check Nodes")
		self.w.slider = Slider((10, 10, -10, 23),
                            tickMarkCount=10,
                            value=0,
                            minValue=0, maxValue=40,
                            callback=self.sliderCallback)
		self.w.textBox = TextBox((10, 40, -10, 17), infoText)
		self.w.open()

	def sliderCallback(self, sender):

		umbral = int(self.w.slider.get())
		self.w.textBox.set("Threshold: " + str(umbral) + " upm")
		def insertArrow(thisLayer, posX, posY, width=30):
			arrow = GSAnnotation.alloc().initWithElementDict_({ "position":"{"+str(posX)+", "+str(posY)+"}", "type":"Circle", "width":width })
			thisLayer.addAnnotation_(arrow)

		def zoneList( master ):
			zoneList = []
			for z in master.alignmentZones:
				zoneOrigin, zoneSize = int(z.position), int(z.size)
				zoneList.append( ( zoneOrigin, zoneOrigin+zoneSize ) )
			return zoneList

		def inZone(thisLayer, masterZones, posX, posY, umbral):
			print ("asa")
			for thisZone in masterZones:
				zoneOrigin = thisZone[0]
				zoneEnd = thisZone[1]

				if zoneOrigin < zoneEnd:
					if posY >= zoneOrigin-umbral and posY <= zoneEnd+umbral:
						return True
				elif zoneOrigin > zoneEnd:
					if posY <= zoneOrigin+umbral and posY >= zoneEnd-umbral:
						return True	
		
		for thisLayer in selectedLayers:
			thisLayer.setAnnotations_(None)
			masterId = thisLayer.associatedMasterId
			master = font.masters[masterId]

			masterZones = zoneList( master )
			

			for thisPath in thisLayer.paths:
				for thisNode in thisPath.nodes:
					if thisNode.type != GSOFFCURVE:
						posY = thisNode.y
						posX = thisNode.x
						
						if inZone (thisLayer, masterZones, posX, posY, umbral=0) is True:
							pass
						elif inZone (thisLayer, masterZones, posX, posY, umbral) is True:
							insertArrow (thisLayer, posX, posY)
							print ("A")
						
nearAlignment()