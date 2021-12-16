# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    def generate(self):

 #On copie la méthode réalisée précédemment dans le fichier "Section.py"
        self.vertices = [ 
                
#                Sommet 1
                [0, 0, 0 ], 
                
                #Sommet 2
                [0, 0, self.parameters['height']],
                
                #Sommet 3
                [self.parameters['width'], 0, self.parameters['height']],
                
                #Sommet 4
                [self.parameters['width'], 0, 0],
                
                #Sommet 5
        		[0,self.parameters['thickness'],0],
                
                #Sommet 6
                [0,self.parameters['thickness'],self.parameters['height']], 
                
                #Sommet 7
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],  
                
                #Sommet 8
                [self.parameters['width'],self.parameters['thickness'],0]
                ]

#Ici, on retire les deux premières faces
        self.faces = [
                [3,7,6,2],
                [0,4,5,1],
                [0,3,7,4],
                [1,2,6,5],
                
                ]  
        
    # Draws the faces                
    def draw(self):        

#On remanie les instructions précédentes en retirant le paramètre d'orientation
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])

#On utilise GL_FILL car on on souhaite cette fois-ci remplir les faces
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        
        for x in self.faces: 
            gl.glBegin(gl.GL_QUADS) 
            
#  On précise cette fois la couleur de remplissage
            gl.glColor3fv([0.5, 0.5, 0.5]) 
            
            gl.glVertex3fv(self.vertices[x[0]])
            gl.glVertex3fv(self.vertices[x[1]])
            gl.glVertex3fv(self.vertices[x[2]])
            gl.glVertex3fv(self.vertices[x[3]])
            gl.glEnd()
        gl.glPopMatrix() 
                      
    
    
    
    