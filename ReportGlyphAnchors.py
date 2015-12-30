#MenuTitle: ReportGlyphAnchors
# -*- coding: utf-8 -*-
__doc__="""
Print in the console the anchors used on selected Glyphs. 
"""
Glyphs.clearLog()
Glyphs.showMacroWindow()
currentLayer = Glyphs.font.selectedLayers[0]
print font.familyName, currentLayer.name


for thisLayer in Glyphs.font.selectedLayers:
    print thisLayer.parent.name + ':',
    for i in thisLayer.anchors:
        print i.name+',',
    print

