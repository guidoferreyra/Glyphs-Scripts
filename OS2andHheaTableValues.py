#MenuTitle: Table Values
# -*- coding: utf-8 -*-
__doc__="""
Fill Font Info custom parameters related to OS/2 and hhea tables.
"""
import GlyphsApp

Glyphs.clearLog()
Glyphs.showMacroWindow()

font = Glyphs.font

selectedLayers = font.selectedLayers
currentLayer = Glyphs.font.selectedLayers[0]

masterID = currentLayer.associatedMasterId
thisMasterAscender = font.masters[masterID].ascender
thisMasterDescender = font.masters[masterID].descender
fontUpm = font.upm
highestGlyph = ['default', 0.00]
lowestGlyph = ['default', 0.00]



for thisLayer in selectedLayers:

	boundHigh = thisLayer.bounds.origin.y + thisLayer.bounds.size.height
	if boundHigh > highestGlyph[1]:
		highestGlyph = thisLayer.parent.name, boundHigh

	boundLow = thisLayer.bounds.origin.y
	if boundLow < lowestGlyph[1]:
		lowestGlyph = thisLayer.parent.name, boundLow

	



# Set Custom Parameters
font.masters[masterID].customParameters['typoAscender'] = thisMasterAscender
print "typoAscender setted:", thisMasterAscender

font.masters[masterID].customParameters['typoDescender'] = thisMasterDescender
print "typoDescender setted:", thisMasterAscender

font.masters[masterID].customParameters['typoLineGap'] = fontUpm * 0.10
print "typoLineGap setted:", fontUpm * 0.10

font.masters[masterID].customParameters['winAscent'] = highestGlyph[1]
print "winAscent setted: based on", str(highestGlyph[0]), str(highestGlyph[1])

font.masters[masterID].customParameters['winDescent'] = abs(lowestGlyph[1])
print "winDescent setted: based on", str(lowestGlyph[0]), str(abs(lowestGlyph[1]))

font.masters[masterID].customParameters['hheaAscender'] = thisMasterAscender
print "hheaAscender setted:", thisMasterAscender

font.masters[masterID].customParameters['hheaDescender'] = thisMasterDescender
print "hheaDescender setted:", thisMasterAscender

font.masters[masterID].customParameters['hheaLineGap'] = fontUpm * 0.10
print "hheaLineGap setted:", fontUpm * 0.10

