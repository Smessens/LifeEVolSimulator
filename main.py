#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:37:42 2020

@author: messenssimon
"""
import time
from time import sleep
import numpy as np 
import random
import math
from UIgame import initPygame,updateUI ,terminateUI

import matplotlib.pyplot as plt
import numpy as np

class herbi:  

    herbiId=0

    def __init__(self,x,y):
        self.foodlevel=herbidict['initfoodlevel']
        self.ID=herbi.herbiId
        herbi.herbiId+=1
        self.x=x
        self.y=y
        self.kind="herbivore"

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



class carni:  

    carniId=0

    def __init__(self,x,y):
        self.foodlevel=carnidict['initfoodlevel']
        self.ID=carni.carniId
        carni.carniId+=1
        self.x=x
        self.y=y
        self.kind="carnivore"

        if(type(board[self.x,self.y])==int): 
            board[self.x,self.y]=self
            self.alive=True
        else:
            self.alive=False
        
        
    def fooddecision(self,x,y,oldx,oldy):
        self.foodlevel-=carnidict['movecost']
        
        if (self.foodlevel>carnidict['reproduce']):
            self.foodlevel-=carnidict['reproduce']
            temp=carni(oldx,oldy)
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
                self.x=tempx
                self.y=tempy
                board[self.x,self.y]=self
                
            elif(board[tempx][tempy]>0): #food
                board[self.x,self.y]=0            
                self.x=tempx
                self.y=tempy
                board[self.x,self.y]=self
            
        else: #no animals
            if(board[tempx][tempy].kind=="herbivore"):
                board[tempx][tempy].alive=False
                self.foodlevel=min(carnidict['maxfood'],self.foodlevel+board[tempx][tempy].foodlevel)
                board[self.x,self.y]=0            
                self.x=tempx
                self.y=tempy
                board[self.x,self.y]=self


            
        self.fooddecision(self.x,self.y,oldx,oldy)
        
        
    def info(self,mode):
        if(mode=="p"):
            print(self.x,self.y,self.foodlevel)
        else:
            return  (self.x,self.y,self.foodlevel,self.ID)
       
    def __repr__(self):
        return "C"+str(self.ID)
    
    def __str__(self):
        return "C"+str(self.ID)
    
    
    
def createAnimals(num):
    global arrAnim
    for i in range (num):
        if(i%ratioherbicarni!=0):
            arrAnim=np.append(arrAnim,herbi(random.randint(0,bSize-1),random.randint(0,bSize-1)))
        else:
            arrAnim=np.append(arrAnim,carni(random.randint(0,bSize-1),random.randint(0,bSize-1)))




def food(): 
    #rot previous
    if(fooddict['lastrot']<=fooddict['rotevery']):
        for (i) in range (bSize):
            for (j) in range (bSize):
                if(type(board[i][j])==int):
                    if(board[i][j]>0):
                        board[i][j]-=1 
        fooddict['lastrot']=0
    fooddict['lastrot']+=1

                
    #spawn
    for i in range (fooddict['number']):
        tempx= random.randint(0,bSize-1)
        tempy= random.randint(0,bSize-1)
        val=fooddict['size']
        
        while(type(board[tempx][tempy])!=int ):
            tempx= random.randint(0,bSize-1)
            tempy= random.randint(0,bSize-1)  

        board[tempx,tempy]+=val
    

    

def printBoard():
    for (i) in range (bSize):
        for (j) in range (bSize):
            print(i,j,type(board[i][j]))
    print("------------")
    
    
def infoAll():
    tot=len(arrAnim)
    
    foodlevel=0
    maxfood=0
    minfood=herbidict['maxfood']
    
    for i in arrAnim:
       x,y,f,ID =i.info("r")
      # i.info("p")
       foodlevel+=f
       maxfood=max(f,maxfood)
       minfood=min(f,minfood)

    if(tot!=0):
        print("            Résumé :" + "Mean food " + str(math.floor(foodlevel/tot)) + " Num Animals " + str(tot) + " Max/min " +  str(maxfood) + " " + str ( minfood))
    else:
        print("All death")

    
def graph (turn,datacarni,dataherbi,datafood):

    
    t = np.arange(0, turn, 1)
    fig, ax1 = plt.subplots()

    ax1.plot(t, dataherbi,color='tab:blue')
    ax1.plot(t, datacarni,color='tab:red')
    

    ax1.axis(ymin=0)
    ax1.set_xlabel('Time [iteration]')
    ax1.set_ylabel('Number of animals')
    
    color = 'tab:green'
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.plot(t,datafood, color=color)
    ax2.axis(ymin=0)
    ax2.set_ylabel('food', color=color)  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor=color)

    
    ax1.set_title('Life simulator')
    
    ax1.grid(True)

    plt.show()
    
    

#def createplayer:
    
def animalTurn():
    delarr=[]
    global arrAnim
    index=0
    for i in arrAnim:
        i.turn()
        if(i.alive==False):
            delarr.append(index)
        index+=1
        
    arrAnim=np.delete(arrAnim,delarr)
        
fooddict= {
  "size": 20,
  "number": 3000,
  "rotevery": 10,
  "lastrot":0
}

carnidict= {
  "initfoodlevel": 200,
  "maxfood": 2000,
  "reproduce": 1200,
  "childcost":500,
  "movecost":8
}

herbidict= {
  "initfoodlevel": 160,
  "maxfood": 1000,
  "reproduce": 600,
  "childcost":200,
  "movecost":2
}

bSize=100
turn=10000
startanimal=1500
ratioherbicarni=2
UI=True
Graph=True
board= np.empty( (bSize,bSize), dtype=object)
board.fill(0)

arrAnim=np.array([])
dataherbi=np.zeros(turn)
datacarni=np.zeros(turn)
datafood=np.zeros(turn)

def lanchgame():
    createAnimals(startanimal)
    infoAll()
    if(UI):
        initPygame(bSize)

#-------------pygame------------------



if __name__ == '__main__':
    start=time.time()
    lanchgame()
    for i in range (turn):
        food()
        animalTurn()
        dataherbi[i]=len([x for x in arrAnim if x.kind=="herbivore"]) #moche
        datacarni[i]=len([x for x in arrAnim if (x.kind=="carnivore")]) #moche
        for (row) in range (bSize):
            for (col) in range (bSize):
                if(type(board[row][col])==int):
                    datafood[i]+=board[row][col]
                        
        if(UI):
            updateUI(board,bSize)
            #sleep(0.5)

        if(i%math.floor(turn/20)==0 and  i!=0):
            
            indice = str(math.floor((np.sum(dataherbi)+np.sum(datacarni))/(time.time()-start)/100))
            
            print(str(math.floor(100*i/turn))+"% , time : "  + str(math.floor(time.time()-start)) + ", indice : "+ indice +", turn per secondes " + str(math.floor(i/(time.time()-start))) )
            
            if(Graph):
                #infoAll()
                graph(turn,datacarni,dataherbi,datafood)
            
            

        

        #print("turn")
    infoAll()
    indice = str(math.floor((np.sum(dataherbi)+np.sum(datacarni))/(time.time()-start)/100))
    print(str(math.floor(100*i/turn))+"% , time : "  + str(math.floor(time.time()-start)) + ", indice : "+ indice +", turn per secondes " + str(math.floor(i/(time.time()-start))) )
 
    #PLOT
    graph(turn,datacarni,dataherbi,datafood)
    
    if(UI):
       terminateUI()

