#MenuTitle: Report anchors off metrics
# -*- coding: utf-8 -*-
__doc__="""
Print in the console a list with the gliphs and anchors off the metrics.
This script is a modification of a mekkablue's script.
"""
Glyphs.clearLog()
Glyphs.showMacroWindow()
font = Glyphs.font
selectedLayers = font.selectedLayers

def checkAnchors (thisLayer):
	
	try:
		# Glyphs 3
		metricsPosition = []
		for metric in thisLayer.metrics():
			metricsPosition.append(metric.position())
	except:
		# Glyphs 2
		thisMaster = thisLayer.associatedFontMaster()
		metricsPosition = [0.0, thisMaster.xHeight, thisMaster.descender, thisMaster.ascender, thisMaster.capHeight]
		try:
			thisMasterSmallheight = float(thisMaster.customParameters['smallCapHeight'])
			metricsPosition.append(thisMasterSmallheight)		
		except:
			pass

	anchorList = []
	for thisAnchor in thisLayer.anchors:
		posy = thisAnchor.position.y
		if posy not in metricsPosition:
			anchorList.append(thisAnchor.name)
	if len(anchorList) != 0:
		print (thisLayer.parent.name + ":" + "%s" % ", ".join(anchorList))
		return True



listOfGlyphs = []
for thisLayer in selectedLayers:
		
    if checkAnchors (thisLayer) is True:
    	listOfGlyphs.append(thisLayer.parent.name)

if listOfGlyphs:
	print ("\nGlyphs with off anchors in this master:\n/%s" % "/".join(listOfGlyphs))
else:
	print ("\nAll anchors on metric lines.")

