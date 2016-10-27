from os import listdir
from os.path import splitext

font = Glyphs.font

layers = font.selectedLayers

mypath = '/Users/guidoferreyra/Desktop/letras'

for fileName in listdir(mypath):
	glifo = splitext(fileName)[0]
	print glifo
	if glifo in font.glyphs:
		for layer in font.glyphs[glifo].layers:
			layer.backgroundImage = GSBackgroundImage(path+"/"+glifo+".jpg")
			layer.backgroundImage.y = -169
	else:
		font.glyphs.append(GSGlyph(glifo))
		layer.backgroundImage = GSBackgroundImage(path+"/"+glifo+".jpg")
		layer.backgroundImage.y = -169
	

