#Imports
import random, time

#Makes a new fighter class
class fighter():
    #initilization function that take in the name of the character and their stats
    def __init__(self, name):
        #Sets all the buffs as normal and names
        self.name = name
        self.defenseMod = 1
        self.speedMod = 1
        self.attackMod = 1
        self.sharingan = False
        #Based on the name of the object adds the corresponding move set dictionary and stats
        if self.name == "Naruto Uzamaki":
            self.hp = 250
            self.chakra = 100
            self.defense = 100
            self.speed = 150
            self.moves = { "Punch" : (20,10, "damage"), "Kunai" : (30, 20, "damage"), "Rasengan" : (70, 60, "damage"), "Shadow Clone Jutsu" : (2 , 60, "buff", "attack"), "Rest" : (25,0,"rest")}
        elif self.name == "Sasuke Uchiha":
            self.hp = 150
            self.chakra = 100
            self.defense = 150
            self.speed = 200            
            self.moves = { "Punch" : (20, 10, "damage"), "Kunai" : (30,20,"damage"), "Chidori" : (80,70, "damage"), "Sharingan" : (0, 75, "buff", "copy"), "Rest" : (25,0,"rest")}
        elif self.name == "Rock Lee":
            self.hp = 200
            self.chakra = 100
            self.defense = 150
            self.speed = 150            
            self.moves = { "Punch" : (30, 10, "damage"), "Kunai" : (40, 20, "damage"), "Kick" : (50,30, "damage"), "8 Gates" : (1.5, 75, "buff", "speed"), "Rest" : (25,0,"rest")}
        else:
            self.hp = 150
            self.chakra = 200
            self.defense = 150
            self.speed = 100            
            self.moves = { "Punch" : (15,10, "damage"), "Kunai" : (10, 5, "damage"), "Sand Armor": (1.5, 50, "buff", "defense"), "Sand Coffin" : (70, 40, "damage"), "Rest" : (25,0,"rest")} 
    #Represent function which prints our all the information about the object
    def __repr__(self):
        return "%s, %d, %d , %d, %s" % (self.name, self.hp, self.chakra, self.defense, self.moves)
    #Attack function
    #Takes in the object itself, the desired target, the selected move, and the random variable which finds out wether or not it would be successful (had to take it out because for some reason it caused crashing)
    def attack(self, other, move, rand):
        #Minuses the chakra cost of the move from the users chakra
        self.chakra = self.chakra - self.moves[move][1]
        time.sleep(1)
        #Determines whether or not the attack was successful
        if (rand - self.moves[move][0]) >= random.randint(0, (other.defense * other.defenseMod)):
            #Subtracts the damage done by the move from the targets health
            other.hp = other.hp - (self.moves[move][0] * self.attackMod)
            print("The attack was successful! %s's health is now %d" % (other.name, other.hp))
            #If the targets sharingan is active adds the selected move to the target's move set
            if other.sharingan == True:
                print("%s copied %s's jutsu!" %(other.name, self.name))
                time.sleep(1)
                #Adds the move to the targets dictionary of moves
                other.moves[move] = self.moves[move]
                #Sets the sharingan to false
                other.sharingan = False
        #If the attack fails gives the failure message        
        else:
            print("The attack misses! %s evaded your attack!" % (other.name))
        time.sleep(1)
    
    #Buff function
    #Takes in self, the list of players, selected move
    def buff(self, players, move):
        #Minuses the chakra cost of the move from the users chakra
        self.chakra = self.chakra - self.moves[move][1]    
        #Based on the area of the buff sets the corresponding modifier to the multiplier of the buff or if it is the sharingan buff sets that to true
        if self.moves[move][3] == "speed":
            self.speedMod = self.moves[move][0]
        elif self.moves[move][3] == "attack":
            self.attackMod = self.moves[move][0]
        elif self.moves[move][3] == "defense":
            self.defenseMod = self.moves[move][0]
        else:
            self.sharingan = True
        #Prints our what has been buffed
        print("%s's %s has been buffed!" %(self.name, self.moves[move][3]))
        time.sleep(1)
        #Checks to see if anybody elses sharingan is active, if it is adds the move to their move set
        for z in players:
            if z.sharingan == True and z.name != self.name:
                print("%s copied %s's justsu!" %(z.name, self.name))
                time.sleep(1)
                z.moves[move] = self.moves[move]
                z.sharingan = False
    
    #Function to debuff all defensive buffs
    #Takes in self
    def defensiveDebuff(self):
        #Sets defense modifier to 1 and switches sharingan off
        self.defenseMod = 1
        self.sharingan = False
        
    #Function to debuff all offensive buffs
    #Takes in self
    def offensiveDebuff(self):
        #Sets speed and attack modifiers to 1
        self.speedMod = 1
        self.attackMod = 1

