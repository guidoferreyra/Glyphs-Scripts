#MenuTitle: AnchorDictionaryMaker
# -*- coding: utf-8 -*-
__doc__="""
Creates a python dictionary with the name of the anchors used on the selected glyphs.
Output to the console
"""
print 'anchorDict = {'
for thisLayer in Glyphs.font.selectedLayers:
    print '"'+thisLayer.parent.name+'"'+ ':(',
    for i in thisLayer.anchors:
        print '"'+i.name+'"'+',',
    print '),'
print '}'