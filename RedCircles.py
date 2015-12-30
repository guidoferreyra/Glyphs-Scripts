#MenuTitle: RedCircles
# -*- coding: utf-8 -*-
__doc__="""
This script searches for control points that are overlapping nodes and marks them with an annotation circle, setting also glyph's color to red.
How to use: select the glyphs and run the script. It works for one master at a time.
A much better tool for this is RedArrows by Jens Kutilek but it only works on Glpyhs 2.
"""

Font = Glyphs.font
selectedLayers = Font.selectedLayers


def insertArrow(layer, x, y, width=30):
	arrow = GSAnnotation.alloc().initWithElementDict_({ "position":"{"+str(x)+", "+str(y)+"}", "type":"Circle", "width":width })
	layer.addAnnotation_(arrow)

for layer in selectedLayers:
 	paths = layer.paths
	
	
	 	
 	for thisPath in paths:
 		nodos = thisPath.nodes
		bcps = [thisNodo for thisNodo in nodos if thisNodo.type == GSOFFCURVE]
		bps = [thisNodo for thisNodo in nodos if thisNodo.type != GSOFFCURVE]
		
		

		for thisNodo in bps:
			for offcurvenode in bcps:
				posx = thisNodo.position.x == offcurvenode.position.x
				posy = thisNodo.position.y == offcurvenode.position.y

				if posx and posy:
					layer.setAnnotations_(None)
					layer.parent.color = (NSNotFound)
					insertArrow(layer, thisNodo.position.x, thisNodo.position.y)
					layer.parent.color = 1

				