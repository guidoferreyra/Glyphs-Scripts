#MenuTitle: Add descriptive names to stylistic sets
# -*- coding: utf-8 -*-
__doc__="""
Based on a given list adds descriptive names to stylistic sets
"""

featureName = [
("ss01","Long descender g"),
("ss02","Cursive k "),
("ss03","Big terminal r"),
("ss04","Curved y "),
("ss05","Inverted y tail"),
("ss06","Baseline aligned J"),
("ss07","Cursive K"),
("ss08","Straight leg K "),
("ss09","Vertical stress zero"),
("ss10","Hairline zero"),
("ss11","Openface arms E, F, L, T, Z, z"),
]


font = Glyphs.font

for feature in featureName:
	try:
		font.features[feature[0]].notes = "Name: "+feature[1]
		print feature[0]+" Name: "+feature[1]
	except:
		pass