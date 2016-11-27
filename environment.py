# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:27:02 2016

@author: Adrien
"""
import numpy as np

class Environment ():
    def __init__(self,nbCol=1,nbRow=1,weight=1):
        self.matrix=np.random.randint(2,size=(nbCol,nbRow))
        #self.matrix=np.zeros((nbCol,nbRow))
        
    def __str__(self):
        return np.array_str(self.matrix)
        
    def modifMatrix(self,position):
        self.matrix[position[0]][position[1]]=8
        
        
    def getCell(self,position):
        return self.matrix[position[0]][position[1]]