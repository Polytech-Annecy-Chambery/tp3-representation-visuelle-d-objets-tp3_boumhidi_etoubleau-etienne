# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):

#On commence par définir les sommets
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

#On définit maintenant les faces à l'aide de matrices
        self.faces = [
                [0,3,2,1],#Face1
                [4,7,6,5],#Face2
                [3,7,6,2],#Face3
                [0,4,5,1],#Face4
                [0,3,7,4],#Face5
                [1,2,6,5],#Face6
                
                ]    
  

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
       
        gl.glPushMatrix()
        
#On translate les valeurs des position
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        
#On utilise GL_LINE car on on souhaite afficher des lignes
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)  
        
#A l'aide d'une boucle for, on parcourt les coordonées de tous les sommets de la face puis on trace la ligne correspondante
        for x in self.faces:
            gl.glBegin(gl.GL_QUADS)
#  On précise la couleur du tracé
            gl.glColor3fv([0, 0, 1])
            gl.glVertex3fv(self.vertices[x[0]]) 
            gl.glVertex3fv(self.vertices[x[1]]) 
            gl.glVertex3fv(self.vertices[x[2]]) 
            gl.glVertex3fv(self.vertices[x[3]]) 
            
            gl.glEnd()
        gl.glPopMatrix()      
                    
    # Draws the faces
    def draw(self):

# On ajoute une condition à la fonction "draw" afin qu'elle dessine les faces uniquement si des sommets sont définit
        if self.parameters['edges']: 
            
# Onpermet l'utilisation de la fonction "drawEdges"            
            self.drawEdges()

#On remanie les instructions précédentes mais pour construire les faces
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        
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
        
        
        
        