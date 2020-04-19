#MenuTitle: AnchorDictionaryMaker
# -*- coding: utf-8 -*-
__doc__="""
Creates a python dictionary with the name of the anchors used on the selected glyphs.
Outputs to the console
"""
output = 'anchorDict = {\n'
for thisLayer in Glyphs.font.selectedLayers:
    output += '\t"'+thisLayer.parent.name+'"'+':('
    for i in thisLayer.anchors:
        output += '"'+i.name+'"'+','
    output += '),\n'
output += '}'

Glyphs.showMacroWindow()
print (output)