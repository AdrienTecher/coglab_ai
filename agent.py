# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:54:37 2016

@author: Adrien
"""

class Agent():
    def __init__(self, env):
        self.position=(1,1)
        self.env=env
        self.env.modifMatrix(self.position)
        self.builtEnv=[8]
        
#    def actualizePosition(self,position):
#        
#        self.env.modifMatrix(position)
        
#    def checkUp(self):
#        posUp=(self.position[0]-1,self.position[1])
#        if self.env.getCell(posUp)==1:
#            self.builtEnv[posUp[0]][posUp[1]]=1    
#            
#    def checkDown(self):
#        posDown=(self.position[0]+1,self.position[1])
#        
    def checkRight(self):
        posRight=(self.position[0],self.position[1]+1)
        self.builtEnv.insert(2,self.env.getCell(posRight))
        
    def checkLeft(self):
        posLeft=(self.position[0],self.position[1]-1)
        self.builtEnv.insert(0,self.env.getCell(posLeft))
        
    def learn(self):
#        try:
#            self.checkUp()
#        except IndexError:
#            print("Up cell does not exist")
#        try:
#            self.checkDown()
#        except IndexError:
#            print("Down cell does not exist")
        try:
            self.checkRight()
        except IndexError:
            print("Right cell does not exist")
        try:
            self.checkLeft()
        except IndexError:
            print("Left cell does not exist")
        
    
    def __str__(self):
        return str(self.builtEnv)