#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:25:30 2020

@author: messenssimon
"""

herbidict= {
  "initfoodlevel": 50,
  "maxfood": 1000,
  "reproduce": 500,
  "childcost":200,
  "movecost":1
}
class herbi:  

    herbiId=0

    def __init__(self,x,y):
        self.foodlevel=herbidict['initfoodlevel']
        self.ID=herbi.herbiId
        herbi.herbiId+=1
        self.x=x
        self.y=y

        if(type(board[self.x,self.y])==int): 
            board[self.x,self.y]=self
            self.alive=True
        else:
            self.alive=False
        
        
    def fooddecision(self,x,y,oldx,oldy):
        self.foodlevel-=herbidict['movecost']
        
        if (self.foodlevel>herbidict['reproduce']):
            self.foodlevel-=herbidict['reproduce']
            temp=herbi(oldx,oldy)
            if (temp.alive):
                global arrAnim
                arrAnim=np.append(arrAnim,temp)
            
            
        if (self.foodlevel<0):
            self.alive=False
            board[self.x,self.y]=0           
                
            
        
    
    def turn(self):
        board[self.x,self.y]=0
        tempx=(self.x+random.randint(-1,1))%bSize
        tempy=(self.y+random.randint(-1,1))%bSize
        oldx=self.x
        oldy=self.y
        
        if(type(board[tempx][tempy])==int): #no animals
            if(board[tempx][tempy]==0): #empty
                board[self.x,self.y]=0            
                self.x=(self.x+random.randint(-1,1))%bSize
                self.y=(self.y+random.randint(-1,1))%bSize
                board[self.x,self.y]=self
                
            elif(board[tempx][tempy]>0): #food
                self.foodlevel=min(herbidict['maxfood'],self.foodlevel+board[tempx][tempy])
                board[self.x,self.y]=0            
                self.x=(self.x+random.randint(-1,1))%bSize
                self.y=(self.y+random.randint(-1,1))%bSize
                board[self.x,self.y]=self
            
        else: #no animals
            board[self.x,self.y]=self
            
        self.fooddecision(self.x,self.y,oldx,oldy)
        
        
    def info(self,mode):
        if(mode=="p"):
            print(self.x,self.y,self.foodlevel)
        else:
            return  (self.x,self.y,self.foodlevel,self.ID)
       
    def __repr__(self):
        return "H"+str(self.ID)
    
    def __str__(self):
        return "H"+str(self.ID)