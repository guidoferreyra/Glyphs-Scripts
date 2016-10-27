#MenuTitle: Close All Tabs
# -*- coding: utf-8 -*-
import GlyphsApp

for i in range(len(Glyphs.font.tabs)):
    del Glyphs.font.tabs[0]