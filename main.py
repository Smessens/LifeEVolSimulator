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
from animals import Animal

import matplotlib.pyplot as plt


UP=0
RIGHT=1
DOWN=2
LEFT=3

from collections import deque  

    
count={
       "food":0,
       "herbivore":0,
       "carnivore":0,
       "omnivore":0,
       "angel":0
}
    
templatedna={
  "mut": 0.01
}
    

def createAnimals(num):
    global arrAnim
    
    for i in range (num):
        tempx=random.randint(0,bSize-1)
        tempy=random.randint(0,bSize-1)
        while(board[tempx][tempy]<0):#find good spot
                   tempx=random.randint(0,bSize-1)
                   tempy=random.randint(0,bSize-1) 
                
        newA=Animal(tempx,tempy,templatedna)
        arrAnim.append(newA)
        board[tempx][tempy]=newA
        count[newA.kind]+=1



def food(): 
    """
    #rot previous
    def rot(a):
        if(type(a)==int):
            return a-1
        return a
    
    if(fooddict['lastrot']<=fooddict['rotevery']):

        fooddict['lastrot']=0
    fooddict['lastrot']+=1
    """
    global board
    if(fooddict['continuous']):
        if(fooddict["perturn"]>=fooddict["actual"]):
            uni=bSize*bSize-count["herbivore"]-count["carnivore"]-count["omnivore"]-count["angel"]
            count["food"]+=uni*fooddict["persquare"]
            board+=fooddict["persquare"]
            fooddict["actual"]=0
        fooddict["actual"]+=1
    
    else:
    #spawn
        for i in range (fooddict['number']):
            tempx= random.randint(0,bSize-1)
            tempy= random.randint(0,bSize-1)
            val=fooddict['size']
            
            
            if(type(board[tempx][tempy])==int ): #dismiss if in use
                board[tempx,tempy]+=val
                count["food"]+=val
    

    

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
    ax1.plot(t, dataomni,color='tab:purple')
    

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
def lookbest(kind,x,y):
    global board
    
    temp=np.zeros(4)

    if(kind=="carnivore"):
        temp[0]=(board[(x-1)%bSize][(y)%bSize].foodlevel/2 if board[(x-1)%bSize][(y)%bSize].kind != "carnivore" else  0) if(type(board[(x-1)%bSize][(y)%bSize])!=int) else 0
        temp[1]=(board[(x)%bSize][(y+1)%bSize].foodlevel/2 if board[(x)%bSize][(y+1)%bSize].kind != "carnivore" else  0)if(type(board[(x)%bSize][(y+1)%bSize])!=int) else 0
        temp[2]=(board[(x+1)%bSize][(y)%bSize].foodlevel/2 if board[(x+1)%bSize][(y)%bSize].kind != "carnivore" else  0)if(type(board[(x+1)%bSize][(y)%bSize])!=int) else 0
        temp[3]=(board[(x)%bSize][(y-1)%bSize].foodlevel/2 if board[(x)%bSize][(y-1)%bSize].kind != "carnivore" else  0)if(type(board[(x)%bSize][(y-1)%bSize])!=int) else 0

    if(kind=="omnivore"):
        temp[0]=(board[(x-1)%bSize][(y)%bSize].foodlevel/2 if board[(x-1)%bSize][(y)%bSize].kind != "carnivore" and board[(x-1)%bSize][(y)%bSize].kind != "omnivore" else  0) if(type(board[(x-1)%bSize][(y)%bSize])!=int) else board[(x-1)%bSize][(y)%bSize]
        temp[1]=(board[(x)%bSize][(y+1)%bSize].foodlevel/2 if board[(x)%bSize][(y+1)%bSize].kind != "carnivore" and board[(x)%bSize][(y+1)%bSize].kind != "omnivore" else  0)if(type(board[(x)%bSize][(y+1)%bSize])!=int) else board[(x)%bSize][(y+1)%bSize]
        temp[2]=(board[(x+1)%bSize][(y)%bSize].foodlevel/2 if board[(x+1)%bSize][(y)%bSize].kind != "carnivore" and board[(x+1)%bSize][(y)%bSize].kind != "omnivore" else  0)if(type(board[(x+1)%bSize][(y)%bSize])!=int) else board[(x+1)%bSize][(y)%bSize]
        temp[3]=(board[(x)%bSize][(y-1)%bSize].foodlevel/2 if board[(x)%bSize][(y-1)%bSize].kind != "carnivore" and board[(x)%bSize][(y-1)%bSize].kind != "omnivore" else  0)if(type(board[(x)%bSize][(y-1)%bSize])!=int) else board[(x)%bSize][(y-1)%bSize]
    
    if(kind=="herbivore"):
        temp[0]=-1000 if(type(board[(x-1)%bSize][(y)%bSize])!=int) else board[(x-1)%bSize][(y)%bSize]
        temp[1]=-1000 if(type(board[(x)%bSize][(y+1)%bSize])!=int) else board[(x)%bSize][(y+1)%bSize]
        temp[2]=-1000 if(type(board[(x+1)%bSize][(y)%bSize])!=int) else board[(x+1)%bSize][(y)%bSize]
        temp[3]=-1000 if(type(board[(x)%bSize][(y-1)%bSize])!=int) else board[(x)%bSize][(y-1)%bSize]
    
    

    a=np.argmax(temp)
    m=np.where(temp==temp[a])
    return np.random.choice(m[0])
    
def animalTurn():
    global arrAnim
    
    temp=deque([])
    temp.clear()
    for i in arrAnim:
        if(i.alive):
            action,direction=i.turn()
            i.turnplayed+=1
            
            
            tempx=i.x
            tempy=i.y
            if(action=="move"):
                direction = lookbest(i.kind,i.x,i.y)

                if(direction==UP):
                    tempx=(tempx-1)%bSize
             
                if(direction==DOWN):
                    tempx=(tempx+1)%bSize
                
                if(direction==LEFT):
                    tempy=(tempy-1)%bSize
                
                if(direction==RIGHT):
                    tempy=(tempy+1)%bSize
                
                
                
                if(i.kind=="carnivore"):
                    if(board[tempx][tempy]>=0):
                        count["food"]-= board[tempx][tempy]

                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy
                        
                    elif(board[tempx][tempy].kind==("carnivore")):
                        pass
                    
                    else:
                        board[tempx][tempy].alive=False
                        board[tempx][tempy].death="Eaten by carni"

                        i.foodlevel=min(i.maxfood,i.foodlevel+ board[tempx][tempy].foodlevel*0.5)
                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy  
                        
                if(i.kind=="omnivore"):
                    if(board[tempx][tempy]>=0):
                        count["food"]-= board[tempx][tempy]

                        i.foodlevel=min(i.maxfood,i.foodlevel+board[tempx][tempy])

                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy
                        
                    elif(board[tempx][tempy].kind==("carnivore")):
                        i.death="Eaten by carni"

                        i.alive=False
                        board[tempx][tempy].foodlevel=min(board[tempx][tempy].maxfood,board[tempx][tempy].foodlevel+i.foodlevel*0.5)
                        board[i.x][i.y]=0                 
                    
                    elif(board[tempx][tempy].kind==("omnivore")):
                        pass
                    
                    else:
                        board[tempx][tempy].alive=False
                        board[tempx][tempy].death="Eaten by omni"

                        i.foodlevel=min(i.maxfood,i.foodlevel+ board[tempx][tempy].foodlevel*0.5)
                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy  
                        
                        
                if(i.kind=="herbivore"):
                    
                    if(board[tempx][tempy]>=0):
                        count["food"]-= board[tempx][tempy]
                        i.foodlevel=min(i.maxfood,i.foodlevel+board[tempx][tempy])
                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy
                        
                    elif(board[tempx][tempy].kind==("carnivore")):
                        i.death="Eaten by carni"

                        i.alive=False
                        board[tempx][tempy].foodlevel=min(board[tempx][tempy].maxfood,board[tempx][tempy].foodlevel+i.foodlevel*0.5)
                        board[i.x][i.y]=0                 
                    
                    elif(board[tempx][tempy].kind==("omnivore")):
                        i.death="Eaten by omni"

                        i.alive=False
                        board[tempx][tempy].foodlevel=min(board[tempx][tempy].maxfood,board[tempx][tempy].foodlevel+i.foodlevel*0.5)
                        board[i.x][i.y]=0                 
                    
                    
                    else:#herbivore
                        pass
                        
                if(i.kind=="angel"):
                    if(board[tempx][tempy]>=0):
                        count["food"]-= board[tempx][tempy]
                        board[i.x][i.y]=0
                        board[tempx][tempy]=i
                        i.x=tempx
                        i.y=tempy
                        
                    elif(board[tempx][tempy].kind==("carnivore")):
                        i.death="Eaten by carni"
                        i.alive=False

                        board[tempx][tempy].foodlevel=min(board[tempx][tempy].maxfood,board[tempx][tempy].foodlevel+i.foodlevel*0.5)
                        board[i.x][i.y]=0                 
                    
                    elif(board[tempx][tempy].kind==("omnivore")):
                        i.death="Eaten by omni"

                        i.alive=False
                        board[tempx][tempy].foodlevel=min(board[tempx][tempy].maxfood,board[tempx][tempy].foodlevel+i.foodlevel*0.5)
                        board[i.x][i.y]=0                 
                    
                    
                    else:#herbivore
                        pass
                    
                    
            if(action=="reproduce"):
                
                if(board[(tempx-1)%bSize][tempy]>=0):
                    newA=Animal((tempx-1)%bSize,tempy,direction)
                    temp.append(newA)
                    board[(tempx-1)%bSize][tempy]=newA
                    i.foodlevel-=i.costreproduce
                    count[newA.kind]+=1

                
                elif(board[(tempx+1)%bSize][tempy]>=0):
                    newA=Animal((tempx+1)%bSize,tempy,direction)
                    temp.append(newA)
                    board[(tempx+1)%bSize][tempy]=newA
                    i.foodlevel-=i.costreproduce
                    count[newA.kind]+=1

                elif(board[tempx][(tempy-1)%bSize]>=0):
                    newA=Animal(tempx,(tempy-1)%bSize,direction)
                    temp.append(newA)
                    board[tempx][(tempy-1)%bSize]=newA
                    i.foodlevel-=i.costreproduce
                    count[newA.kind]+=1

                
                elif(board[tempx][(tempy+1)%bSize]>=0):
                    newA=Animal(tempx,(tempy+1)%bSize,direction)
                    temp.append(newA)
                    board[tempx][(tempy+1)%bSize]=newA
                    i.foodlevel-=i.costreproduce
                    count[newA.kind]+=1

                
                
                
            #fooddecision
            i.foodlevel-=i.movecost
            if(i.foodlevel<0):
                i.death="starved"
                i.alive=False
                board[i.x][i.y]=0   
           
            elif(i.turnplayed>oldage): #si vieux une chance ssur 100 de mourir
                if(random.randint(1,oldage//10)==1):
                    i.death="Old age"
                    i.alive=False
                    board[i.x][i.y]=0   
    
    
    
    for j in range (len(arrAnim)-1,-1,-1):
        if(arrAnim[j].alive==False):
            count[arrAnim[j].kind]-=1
            arrAnim.remove(arrAnim[j].ID)
            
    if(len(temp)>0):
        for e in temp:
            arrAnim.append(e)
        

        
        
#-----Null Variable initiaton
timerFood=0
timerData=0
timerAnimal=0
timerUI=0


    
    
fooddict= {
  "size": 10,
  "number": 8000,
  "rotevery": 10,
  "lastrot":0,
  "continuous":True,
  "persquare":1,
  "perturn":10,
  "actual":0
}

carnidict= {
  "initfoodlevel": 300,
  "maxfood": 2000,
  "reproduce": 1000,
  "childcost":500,
  "movecost":8
}

herbidict= {
  "initfoodlevel": 160,
  "maxfood": 1000,
  "reproduce": 400,
  "childcost": 200,
  "movecost":5
}

bSize=400
turn=2000
startanimal=1000
minimanimal=10
oldage=1000
ratioherbicarni=4
UI=True
UIevery=100
Graph=True
board= np.empty( (bSize,bSize), dtype=object)
board.fill(0)
minimumTime=0.00

arrAnim= deque([])   

dataherbi=np.zeros(turn)
dataomni=np.zeros(turn)
datacarni=np.zeros(turn)
datafood=np.zeros(turn)



def lanchgame():
    createAnimals(startanimal)
    infoAll()
    for i in range (10):
        food()
    if(UI):
        initPygame(bSize)
        updateUI(board,bSize)



#-------------pygame------------------




if __name__ == '__main__':
    start=time.time()
    lanchgame()

    
    for i in range (turn):
        tick=time.time()
        timerFood-=time.time()
        food()
        timerFood+=time.time()

        timerAnimal-=time.time()
        animalTurn()
        timerAnimal+=time.time()
        if(len(arrAnim)<minimanimal):
                print("RESTART ",i)
                createAnimals(minimanimal)
        
        if(Graph):
            timerData-=time.time()
            dataherbi[i]=count["herbivore"]
            dataomni[i]=count["omnivore"]
            datacarni[i]=count["carnivore"]
            datafood[i]=count["food"]
            

            timerData+=time.time()


        if(UI and i%UIevery==0):
            timerUI-=time.time()

            updateUI(board,bSize)
            while(time.time()-tick<minimumTime):
                wasting='time'
            timerUI+=time.time()


        if(i%math.floor(turn/20)==0 and  i!=0):            
            indice = str(math.floor((np.sum(dataherbi)+np.sum(datacarni))/(time.time()-start)/100))
            print(str(math.floor(100*i/turn))+"% , time : "  + str(math.floor(time.time()-start)) + ", indice : "+ indice +", turn per secondes " + str(math.floor(i/(time.time()-start))),"Timerfood " + str(math.floor(timerFood)) + "% TimerData " + str(math.floor(timerData*100/(time.time()-start))) + "% timerAnimal "+ str(math.floor(timerAnimal*100/(time.time()-start))) + "% timerUI " +str(math.floor(timerUI*100/(time.time()-start))),"%" )
            print()
            print(arrAnim[random.randint(0,len(arrAnim)-1)].printDNA())
            print()

            if(Graph):
                #infoAll()
                graph(turn,datacarni,dataherbi,datafood)
     
        
            
            

        

    infoAll()
    print(arrAnim[random.randint(0,len(arrAnim)-1)].printDNA())
    indice = str(math.floor((np.sum(dataherbi)+np.sum(datacarni))/(time.time()-start)/100))
    print(str(math.floor(100*i/turn))+"% , time : "  + str(math.floor(time.time()-start)) + ", indice : "+ indice +", turn per secondes " + str(math.floor(i/(time.time()-start))) )
    print("Timer food " + str(math.floor(timerFood)) + " TimerData " + str(math.floor(timerData)) + " timerAnimal "+ str(math.floor(timerAnimal)) + " timerUI " +str(math.floor(timerUI)))

    #PLOT
    graph(turn,datacarni,dataherbi,datafood)
    
    if(UI):
       terminateUI()

