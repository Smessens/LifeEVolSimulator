#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:05:03 2020

@author: messenssimon
"""

import random

ID=-1


Valudict= {
  "minimumcostreproduce": 10,
  "costHerbi": 100,
  "costCarni": 300,
  "costHerbiMove": 1,
  "costCarniMove": 6,
  "movecost": 0.1,
  "childpercent":0.8,
  "movecostangel":1,
  "omnimul":10
  
}

class Animal:  

    def __init__(self,x,y,dna):
        global ID
        self.ID=ID
        ID-=1
        self.x=x
        self.y=y
        self.alive=True
        self.turnplayed=0
        mut=0.01
        costreproduce=Valudict["minimumcostreproduce"]
        movecost=Valudict["movecost"]
        
        if("mut"in dna ):
            if(mut==0):#disabled
                self.mut=0
            else:
                self.mut=min(0.0001,dna['mut']*random.randint(-1,1)*dna['mut'])
        else:
            self.mut=random.randint(1,100)/1000 #max 10%

        
        if("herbival"in dna ):
            self.herbival=dna['herbival']*(1+random.randint(-1,1)*self.mut)
        else:
            self.herbival=random.randint(-1,1)
        
        if(self.herbival>0):
            self.herbi=True
            costreproduce+=Valudict[ "costHerbi"]
            movecost+=Valudict["costHerbiMove"]
        else:
            self.herbi=False
            
        
        if("carnival"in dna ):
            self.carnival=dna['carnival']*(1+random.randint(-1,1)*self.mut)
        else:
            self.carnival=random.randint(-1,1)
        
        if(self.carnival>0):
            self.carni=True
            costreproduce+=Valudict[ "costCarni"]
            movecost+=Valudict["costCarniMove"]

        else:
            self.carni=False
        
        if("reserveMother"in dna ):
            self.reserveMother=max(1,dna['reserveMother']*(1+random.randint(-1,1)*self.mut))
        else:
            self.reserveMother=random.randint(0,1000)
            
        if("reserveDau"in dna ):
            self.reserveDau=max(1,dna['reserveDau']*(1+random.randint(-1,1)*self.mut))
        else:
            self.reserveDau=random.randint(0,1000)   
            
        self.foodlevel=self.reserveDau*Valudict["childpercent"]

        
        self.reproduce=self.reserveMother+self.reserveDau+costreproduce
        self.movecost=movecost
        self.costreproduce=costreproduce
        
        if("maxfood" in dna ):
            self.maxfood=max(self.reproduce+1,dna['reserveDau']*(1+random.randint(-1,1)*self.mut))
        else:
            self.maxfood=self.reproduce+random.randint(0,1000)   
        
        if(self.herbi and self.carni):
            self.kind="omnivore"
            self.movecost=movecost*Valudict["omnimul"]
            
        elif(self.carni):
            self.kind="carnivore"
        elif(self.herbi):
            self.kind="herbivore"
        else:
            self.kind="angel"
            self.movecost=Valudict["movecostangel"]
            
        self.lastmove=0
        self.death=None
            
        self.dna={
          "mut": self.mut,
          "kind":self.kind,
          "foodlevel":self.foodlevel,
          "herbival":self.herbival,
          "carnival":self.carnival,
          "reserveMother": self.reserveMother,
          "reserveDau": self.reserveDau,
          "maxfood":self.maxfood,
          "movecost":self.movecost,
          "ID":self.ID,
          "alive":self.alive,
          "turnplayed":self.turnplayed,
          "lastmove":self.lastmove,
          "death":self.death,
          "reproduce":self.reproduce
          
        }

        
    
    def turn(self):
        if(self.foodlevel>=self.reproduce):
            self.lastmove="reproduce",self.dna
            return self.lastmove
        else:#randomizedirection
    
            self.lastmove=("move",random.randint(0,3))
            return self.lastmove
        
    def printDNA(self):
        self.dna={
          "mut": self.mut,
          "kind":self.kind,
          "foodlevel":self.foodlevel,
          "herbival":self.herbival,
          "carnival":self.carnival,
          "reserveMother": self.reserveMother,
          "reserveDau": self.reserveDau,
          "maxfood":self.maxfood,
          "ID":self.ID,
          "alive":self.alive,
          "turnplayed":self.turnplayed,
          "lastmove":self.lastmove,
          "death":self.death
        }
        print(str(self.dna))


    def info(self,mode):
        if(mode=="p"):
            print(self.x,self.y,self.foodlevel)
        else:
            return  (self.x,self.y,self.foodlevel,self.ID)
       
    #overidding fuction for easier manipulation
    def __repr__(self):
        return str(self.ID)
    
    def __str__(self):
        return str(self.ID)
    
    def __eq__(self, obj):
        return obj == self.ID
    
    def __ne__(self, obj):
        return obj != self.ID
    
    def __add__(self,a):
        #notToday
        return self
            
    def __mul__(self,a):
        #notToday
        return self
    def __sub__(self,a):
        #notToday
        return self
    
    def __truediv__(self,a):
        #notToday
        return self
    
    def __lt__(self,other):
        return (self.ID<other)

    def __le__(self,other):
        return(self.ID<=other)

    def __gt__(self,other):
        return(self.ID>other)
    
    def __ge__(self,other):
        return(self.ID>=other)
