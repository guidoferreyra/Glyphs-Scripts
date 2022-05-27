#MenuTitle: Automatic OT Classes
# -*- coding: utf-8 -*-
__doc__="""
Create and update Opentype classes based on information (name of class and text in glpyh name) stored in the custom parameter "otFeatureClass".
Useful for update continuously growing classes during the development. Also can create OT class based on another class finding and replacing a value.
Examples of custom parameters:

Property: otClass
Value: new_class_name;text_in_glyphname
	   ss01;alt1

Property: otClassCopyEdit
Value: new_class_name;base_class_name;find_text;replace_text;
	   ss02;ss01;alt1;alt2;

"""

from GlyphsApp import *

font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

def updateClass(className, text):
	listOfClasses = Glyphs.font.classes
	lisOfClassesNames = [ c.name for c in Glyphs.font.classes ]
	
	textInName = text
	glyphsForClass = []

	for glyph in font.glyphs:
		if glyph.name.endswith(textInName):
			glyphsForClass.append(glyph.name)
		
	classCode = ' '.join(glyphsForClass)
	if len(glyphsForClass) != 0:
		if className in lisOfClassesNames:
			print ("Updated", className, "with:\n", classCode, "\n")
			listOfClasses[ className ].code = classCode
		else:
			print ("New", className, "with:\n", classCode, "\n")
			font.classes.append(GSClass(className, classCode))
	else:
		print ("No glyph names with the text: " + text + "\n")
		
		

def copyAndEdit (newClass, oldClass, oldText, newText):
	listOfClasses = Glyphs.font.classes
	lisOfClassesNames = [ c.name for c in Glyphs.font.classes ]
	
	
	oldClassCode = listOfClasses[ oldClass ].code
	
	newClassCode = oldClassCode.replace(oldText.replace('"', ''), newText.replace('"', ''))
	
	if newClass in lisOfClassesNames:
		print ("Updated", newClass, "with:\n", newClassCode, "\n")
		listOfClasses[ newClass ].code = newClassCode
	else:
		print ("New", newClass, "with:\n", newClassCode, "\n")
		font.classes.append(GSClass(newClass, newClassCode))
	
	
	
	


for parameter in font.customParameters:
	if parameter.name == "otClass":
		value = parameter.value.split(";")
		name, text = value[0], value[1]	
		updateClass (name, text)
	elif parameter.name == "otClassCopyEdit":
		value = parameter.value.split(";")
		newClass = value[0]
		oldClass = value[1]
		oldText = value[2]
		newText = value[3]		

#		print newClass, oldClass, oldText, newText
		copyAndEdit (newClass, oldClass, oldText, newText)
			

