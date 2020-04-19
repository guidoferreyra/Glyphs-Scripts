#MenuTitle: Create OT Class
# -*- coding: utf-8 -*-
__doc__="""
(UI) Create an Opentype Class with glyphs containing an specified text.
This script uses code from Mekkablue's "Make OT class from selected glyphs".
"""

from GlyphsApp import *
from vanilla import *


font = Glyphs.font

class createOtClass(object):

	def __init__(self):
		
		self.w = Window((240, 145), "Create Ot Class")
		self.w.label = TextBox((10, 10, -120, 20), "text in name:")
		self.w.textInName = EditText((-130, 10, -10, 20), "", sizeStyle='small')
		self.w.label2 = TextBox((10, 40, -120, 20), "Class name:")
		self.w.class_name = EditText((-130, 40, -10, 20), "", sizeStyle='small', callback=self.buttonCheck)
		self.w.box = Box((10, 70, -10, 36))
		self.w.box.infoBox = TextBox((0, 0, -0, -0), "", alignment='left', sizeStyle='small')
		self.w.createButton = Button((10, 115, -10, 20), "Create Class", callback=self.buttonCallback)
		
		self.w.open()
		self.buttonCheck( self.w.class_name )


	def buttonCheck(self, sender):
		className = sender.get()
		lisOfClassesNames = [ c.name for c in Glyphs.font.classes ]

		#print existingClasses
		
		if className in lisOfClassesNames:
			self.w.createButton.enable( True )
			self.w.box.infoBox.set( "Class name already exists. It will overwrite" )
		elif len( className ) == 0 :
			self.w.createButton.enable( False )
			self.w.box.infoBox.set( "Class name empty." )
		elif self.checkstring( className ):
			self.w.createButton.enable( True )
			self.w.box.infoBox.set( "Class name appears to be ok." )
		elif className[0] in "0123456789":
			self.w.createButton.enable( False )
			self.w.box.infoBox.set( "Class name must not start with a figure." )
		else:
			self.w.createButton.enable( False )
			self.w.box.infoBox.set( "Illegal characters. Only use A-Z, a-z, figures, period, underscore." )

	def checkstring(self, teststring, ok=True):
		allowedchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890._"
		
		if len( teststring ) > 1 :
			return self.checkstring( teststring[:-1], ok ) and ( teststring[-1] in allowedchars )
		else:
			# first char must not be a figure
			return ( teststring[-1] in allowedchars and teststring[-1] not in "1234567890" )


	def buttonCallback(self, sender):
		listOfClasses = Glyphs.font.classes
		lisOfClassesNames = [ c.name for c in Glyphs.font.classes ]
		className = str( self.w.class_name.get() )
		textInName = str( self.w.textInName.get() )
		gliphstForClass = []

		print (textInName)
		for glyph in font.glyphs:
			if textInName in glyph.name:
				gliphstForClass.append(glyph.name)
		
		classCode = ' '.join(gliphstForClass)

		if className in lisOfClassesNames:
			print ("Updating class:", className, "with this glyphs:", classCode)
			listOfClasses[ className ].code = classCode
		else:
			font.classes.append(GSClass(className, classCode))
			print ("Created class:", className, "with this glyphs:", classCode)




createOtClass()

