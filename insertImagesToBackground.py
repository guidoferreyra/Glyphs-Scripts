#MenuTitle: Insert images in background
# -*- coding: utf-8 -*-
__doc__="""
In the dialog box select images to insert as background. Images must be named with the corresponding glyphname (ie. a.jpg) in case the glyph is not in the font the script will create it.
"""
from os import listdir
from os.path import splitext
from os.path import split

font = Glyphs.font

font.disableUpdateInterface()


paths = GetOpenFile(
	message = "Select image:",
	allowsMultipleSelection = True,
	filetypes = ["jpeg", "png", "tif", "gif", "pdf"]
)

for imageFilePath in paths:
	fileName = split(imageFilePath)
	glyphName = splitext(fileName[1])[0]

	if glyphName in font.glyphs:
		thisGlyph = font.glyphs[glyphName]
		for layer in thisGlyph.layers:
			layer.backgroundImage = GSBackgroundImage(imageFilePath)
			thisGlyph.updateGlyphInfo()
	else:
		font.glyphs.append(GSGlyph(glyphName))
		thisGlyph = font.glyphs[glyphName]
		for layer in thisGlyph.layers:
			layer.backgroundImage = GSBackgroundImage(imageFilePath)
			thisGlyph.updateGlyphInfo()			
	
	print ("Added image to", glyphName, "background. Be sure to have View> Show image activated.")

font.enableUpdateInterface()
