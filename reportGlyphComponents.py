#MenuTitle: Report Glyph Components
# -*- coding: utf-8 -*-
__doc__="""
Prints in the console the components used on selecteds glyphs. 
"""
Glyphs.clearLog()

font = Glyphs.font
currentLayer = Glyphs.font.selectedLayers[0]
print font.familyName, currentLayer.name


for thisLayer in Glyphs.font.selectedLayers:
    print thisLayer.parent.name + ':',
    for i in thisLayer.components:
        print i.componentName+',',
    print

Glyphs.showMacroWindow()