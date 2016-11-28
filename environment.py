# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:27:02 2016

@author: Adrien
"""
#import numpy as np

class Environment ():
    def __init__(self,nbCol=1,nbRow=1,weight=1):
        wall=[]
        for col in range(nbCol+2):
            wall.append(-1)
        self.matrix=[wall,wall]
        for row in range(1,nbRow+1):
            self.matrix.insert(1,[-1,-1])
        for row in range(1,nbRow+1):
            for j in range(nbCol):
                self.matrix[row].insert(1,0)
        
    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix])
        
    def modifMatrix(self,position):
        self.matrix[position[0]][position[1]]=8
        
        
    def getCell(self,position):
        return self.matrix[position[0]][position[1]]