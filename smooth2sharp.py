#MenuTitle: Smooth2Sharp
# -*- coding: utf-8 -*-
__doc__="""
The script searches smooth nodes with disaligned handles and changes them to sharp.
"""

import math

Font = Glyphs.font
selectedLayers = Font.selectedLayers

for layer in selectedLayers:
    paths = layer.paths
    
    for thisPath in paths:
        numOfNodes = len(thisPath.nodes)
        
        for thisNodeIndex in range(numOfNodes):
                thisNode = thisPath.nodes[ thisNodeIndex ]
                prevNode = thisPath.nodes[ (thisNodeIndex - 1) % numOfNodes ]
                nextNode = thisPath.nodes[ (thisNodeIndex + 1) % numOfNodes ]

                posx = thisNode.position.x
                posy = thisNode.position.y
                prevposx = prevNode.position.x
                prevposy = prevNode.position.y
                
                nextposx = nextNode.position.x
                nextposy = nextNode.position.y
                          
                #1er. Filtro. Fuera OFFCURVES Y SHARPS
                if thisNode.type == GSCURVE and thisNode.connection == GSSMOOTH:
                        
                        #2do. Filtro. Fuera ortogonales
                        if not (( posx - prevposx ) + ( posx - nextposx ) == 0.0 or ( posy - prevposy ) + ( posy - nextposy ) == 0.0):

                            #triangulo 1
                            ladoX1 = prevposx - posx
                            ladoY1 = prevposy - posy
                                                            
                            #triangulo 2
                            ladoX2 = nextposx - posx
                            ladoY2 = nextposy - posy
                            
                            #3er. Filtro. Fuera nodos con 1 tirador sobre Y o X
                            if ladoY1 == 0.0 or ladoY2 == 0.0 or ladoX1 == 0.0 or ladoX2 == 0.0:
                                thisNode.connection = GSSHARP

                            else:
                                #Tangente Angulo Triangulo1
                                angle1 = ladoY1 / ladoX1
                                
                                #Tangente Angulo Triangulo2
                                angle2 = ladoY2 / ladoX2
                                
                                #Redondeo Angulo1
                                ceil1=(math.ceil(angle1*100)/100)

                                #Redondeo Angulo2
                                ceil2=(math.ceil(angle2*100)/100)

                                #Resta de los redondeos                         
                                resta = ceil1 - ceil2
                                
                                #Limite permitido 
                                if resta > 0.1 or resta < -0.1:
                                    thisNode.connection = GSSHARP