#MenuTitle: Create accented versions of glyph
# -*- coding: utf-8 -*-
__doc__="""
Based on a dictionary adds to the font the accented versions of the selected glyphs.
"""

font = Glyphs.font

layers = font.selectedLayers

listOfGlyphs = []

Glyphs.clearLog()
Glyphs.showMacroWindow()


diacriticsDict = {
"a":("acute", "breve", "circumflex", "dieresis", "grave", "macron", "ogonek", "ring", "tilde"),
"c":("acute", "caron", "cedilla", "dotaccent"),
"d":("caron","croat"),
"e":("acute", "caron", "circumflex", "dieresis", "dotaccent", "grave", "macron", "ogonek"),
"g":("breve", "commaaccent", "dotaccent"),
"h":("bar",),
"i":("acute", "circumflex", "dieresis", "dotaccent", "grave", "macron", "ogonek",),
"k":("commaaccent",),
"l":("acute", "caron", "commaaccent","slash",),
"n":("acute","caron","commaaccent","tilde"),
"o":("acute", "circumflex", "dieresis", "grave", "hungarumlaut", "macron", "slash", "tilde"),
"r":("acute", "caron", "commaaccent"),
"s":("acute", "caron", "cedilla", "commaaccent"),
"t":("bar", "caron", "cedilla", "commaaccent"),
"u":("acute", "circumflex", "dieresis", "grave", "hungarumlaut", "macron", "ogonek", "ring"),
"w":("acute", "circumflex", "dieresis", "grave"),
"y":("acute", "circumflex", "dieresis", "grave"),
"z":("acute", "caron", "dotaccent")
}



def addGlyphs(currentGlyph):
	if "." in currentGlyph:
		baseGlyph = currentGlyph.split(".")[0]
	for diacritic in diacriticsDict[baseGlyph]:
		if "." in currentGlyph:
			newGlyphName = currentGlyph.replace('.', diacritic+'.')
			print newGlyphName
			#font.glyphs.append(GSGlyph(newGlyphName))
			#for master in font.masters:
			#	newLayer = font.glyphs[newGlyphName].layers[master.id]
			#	newLayer.makeComponents()
		else:
			newGlyphName = currentGlyph+diacritic
			print newGlyphName
			#font.glyphs.append(GSGlyph(newGlyphName))
			#for master in font.masters:
			#	newLayer = font.glyphs[newGlyphName].layers[master.id]
			#	newLayer.makeComponents()
	

for layer in layers:
	glyphName = layer.parent.name
	listOfGlyphs.append(glyphName)
	addGlyphs(glyphName)