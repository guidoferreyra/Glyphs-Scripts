#MenuTitle: CompareSets
# -*- coding: utf-8 -*-
__doc__="""
Shows diffrences between glyph sets and allows to add glyphs to fonts.
"""

from GlyphsApp import *
from vanilla import *

# estas cosas afuera se vuelven variables globales, estás seguro que no pueden estar adentro de otro lugar?
font1 = Glyphs.fonts[0]
font2 = Glyphs.fonts[1]
masterName1 = font1.masters[0].name
masterName2 = font2.masters[0].name


#Esta clase la agreugue porque Vanilla, el modulo de UI, dice que hay que hacerlo asi. Todavia no se lo que es una clase.
class ListDemo(object):
	
	# acá están como atributos del objeto
	lista1 = []
	lista2 = []
	
	def __init__(self):
		# Acá seteas las listas. Ahora en teoría se podrían actualizar cada vez que llames el método
		# init, lo cuál no suele pasar muy seguido(en gral una vez) 
		self.createLists()
		DiffLists = (self.lista1, self.lista2)

		#User interface elements
		self.w = Window((330, 320),"Compare Sets", minSize=(330,320), maxSize=(330,1000))
		self.w.textBox = TextBox((10, 10, -10, 34), "Missing on \n" + font1.familyName + " " + masterName1)
		self.w.myList = List((10, 55, 150, -40), self.lista2)
		self.w.button = Button((10, -30, 150, 20), "Add to font",
							callback=self.button1Callback)
					 
		self.w.textBox2 = TextBox((170, 10, -10, 34), "Missing on \n" + font2.familyName + " " + masterName2)                     
		self.w.myList2 = List((170, 55, 150, -40), self.lista1)
		self.w.button2 = Button((170, -30, 150, 20), "Add to font",callback=self.button2Callback1)          
		self.w.open()

	#Respuestas de los botones
	def button1Callback(self, sender):
		seleccion = self.w.myList.getSelection()
		trash = []
		for i in seleccion:
			name = self.w.myList.__getitem__(i)
			font1.glyphs.append(GSGlyph(name))
			trash.append(name)
			#funcion de Glyphs para crear componentes (ignora esto)
			for layer in font1.glyphs[name].layers:
				layer.beginChanges()
				layer.makeComponents()
				layer.endChanges()

		for ii in trash:
			self.w.myList.remove(ii)	
			


	def button2Callback1(self, sender):
		seleccion = self.w.myList.getSelection()
		trash = []
		for i in seleccion:
			name = self.w.myList2.__getitem__(i)
			font2.glyphs.append(GSGlyph(name))
			trash.append(name)
			#funcion de Glyphs para crear componentes (ignora esto)
			for layer in font1.glyphs[name].layers:
				layer.beginChanges()
				layer.makeComponents()
				layer.endChanges()

		for ii in trash:
			self.w.myList.remove(ii)
	
	def createLists(self):
		# Como método, hace lo mismo que hacía antes como función, solo que
		# ahora es un método de la clase y modifica los atributos lista1 y
		# lista2 de forma interna digamos, no necesita devolver ningún valor.
		#llena las listas con todos los nombres de los glifos de cada fuente
		for a in font1.glyphs:
			self.lista1.append(a.name) #A, B, C, D, etc.
		for a in font2.glyphs:
			self.lista2.append(a.name)
		#Hago sets de las listas
		font1Set = set(self.lista1)
		font2Set = set(self.lista2)
		
		#Hace sets con las difrencias
		OneDiff = font1Set.difference(font2Set)
		TwoDiff = font2Set.difference(font1Set)

		#Transforma los sets en listas de nuevo
		self.lista1 = list(OneDiff)
		self.lista2 = list(TwoDiff)
		
Glyphs.clearLog()
Glyphs.showMacroWindow()
ListDemo()