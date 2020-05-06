#Imports
import random, winsound, threading, time, Fighters
#Tkinter import
from Tkinter import *
#Treading imports which allows me to run functions at the same time
from threading import Thread
#Tkinter set up
master = Tk()
w = Canvas(master, width = 1000, height = 600, bg = "white")
w.pack()
#Imports necessary images for Tkinter
title = PhotoImage(file = "title.gif")
select = PhotoImage(file = "select.gif")
fight = PhotoImage(file = "setting.gif")

#Intro function
#Runs the instructions and shows the title screen
def intro():
    #Shows the title
    a = w.create_image(500, 300, image = title)
    #Updates the window
    w.update()
    print("WELCOME TO THE NARUTO FIGHTING ARENA")
    time.sleep(1)
    print("\n")
    print("Instructions:")
    print("1. You can have 2-4 players at a time.")
    time.sleep(1)
    print("2. Defensive buffs (things that buff defense or sharingan) last only one turn cycle")
    time.sleep(1)
    print("3. Offensive buffs (moves that buff speed or attack) last until you attack")
    time.sleep(1)
    print("4. When calling on a move. Write exactly what the move is listed as")
    time.sleep(1)
    print("5. The info about moves is organized with the amount of damage it does or the multiplier first, then the chakra cost, then the type of move, and finally, if there is a slot the area the buff is applied to")
    time.sleep(1)
    print("6. You can only play one of each character")
    time.sleep(1)
    print("7. For information on your characters health, chakra, etc. look to Tkinter window")
    time.sleep(1)
    print("8. Do not worry if your stats on the Tkinter window do not change after a buff. The buffs only are taken into account when needed.")
    time.sleep(1)
    print("9. Sharingan will only copy one move per activation.")
    time.sleep(1)
    #Closes the Tkinter and gets rid of the title
    w.delete(a)
    mainloop()
    
#Function to run the opening music
def introMusic():
    return
    
#Function that runs the character select
def characterSelect():
    #Shows the characters you can choose from
    a = w.create_image(400,300, image = select)
    w.update()
    #Creates empty list for the player information and stats
    players = []
    #Creates empty list for the player names which makes it easy to do Tkinter elements
    playernames = []
    print
    #Gets the amount of players
    repeat = True
    while repeat == True:
        print("How many players? MAX 4 / MIN 2")
        try:
            participants = input()
            if 2 <= participants <= 4:
                repeat = False
            else:
                print("That is not possible")
        except:
            print("Incorrect inputs")
    #Finds out who each player is going to player
    for i in range(participants):
        repeat = True
        while repeat == True:
            #Asks the player which of the options they want to play
            print("PLAYER NUMBER", i + 1)
            print("Who do you want to play as? Rock Lee? Naruto Uzamaki? Sasuke Uchiha? Gaara of the Sand?")
            x = raw_input().lower()
            #Checks to see if the entry is one of the options and that no one else has already selected that character
            if x == "lee" and "lee" not in playernames or x == "rock lee" and "lee" not in playernames:
                #Creates the character with the corresponding statistics
                i = Fighters.fighter("Rock Lee")
                #Adds the players character name to the list of player names
                playernames.append("lee")
                repeat = False
            elif x == "naruto" and "naruto" not in playernames or x == "naruto uzamaki" and "naruto" not in playernames:
                i = Fighters.fighter("Naruto Uzamaki")
                playernames.append("naruto")
                repeat = False
            elif x == "sasuke" and "sasuke" not in playernames or x == "sasuke uchiha" and "sasuke" not in playernames:
                i = Fighters.fighter("Sasuke Uchiha")
                playernames.append("sasuke")
                repeat = False
            elif x == "gaara" and "gaara" not in playernames or x == "gaara of the sand" and "gaara" not in playernames:
                i = Fighters.fighter("Gaara of the Sand")
                playernames.append("gaara")
                repeat = False
            else:
                #Tells the user that that wasnt one of the options
                print("That is not an option. Sorry.")
        #Adds the players information to the correspondint list        
        players.append(i)
    #Returns the two lists
    return players, playernames

#Function that refreshes the stats on the Tkinter window
def statShow(player):
    #Refreshes the specific characters stats
    if player.name == "Naruto Uzamaki":
        #Creates the blank rectangle for the info to be written on in the right spot. Have to cover the old one with a new one everytime so that the text does not run over itself
        j = w.create_rectangle(10,10,210,110, fill = "white", outline = "black")
        #Writes the correct and updated information in
        q = w.create_text(57, 55, text = "%s \nHealth: %d \nChakra: %d \nDefense: %d \nSpeed: %d \nSharingan: %s" %(player.name, player.hp, player.chakra, player.defense, player.speed, player.sharingan))
    elif player.name == "Sasuke Uchiha":
        k = w.create_rectangle(260,10,460,110, fill = "white", outline = "black")
        e = w.create_text(307,55, text = "%s \nHealth: %d \nChakra: %d \nDefense: %d \nSpeed: %d \nSharingan: %s" %(player.name, player.hp, player.chakra, player.defense, player.speed, player.sharingan))
    elif player.name == "Rock Lee":
        l = w.create_rectangle(510,10,710,110, fill = "white", outline = "black")
        e = w.create_text(555,55, text = "%s \nHealth: %d \nChakra: %d \nDefense: %d \nSpeed: %d \nSharingan: %s" %(player.name, player.hp, player.chakra, player.defense, player.speed, player.sharingan))
    else:
        k = w.create_rectangle(760,10,960,110, fill = "white", outline = "black")
        r = w.create_text(815,55, text = "%s \nHealth: %d \nChakra: %d \nDefense: %d \nSpeed: %d \nSharingan: %s" %(player.name, player.hp, player.chakra, player.defense, player.speed, player.sharingan))
    #Updates the window showing the new stats    
    w.update()

#Function to play the select screen music
def selectMusic():
    return

#Function that actual runs the game or match
#Takes in the two lists of player info and the names of the players
def match(players, playernames):
    #Randomizes the order of players and thus turn order
    random.shuffle(players)
    #Creates the fight background
    a = w.create_image(500,300, image = fight)
    w.update()
    #Shows the character sprites of the active players
    if "naruto" in playernames:
        naruto = PhotoImage(file = "naruto.gif")
        b = w.create_image(100, 300, image = naruto)
    if "sasuke" in playernames:
        sasuke = PhotoImage(file = "sasuke.gif")
        c = w.create_image(360, 300, image = sasuke)
    if "lee" in playernames:
        lee = PhotoImage(file = "lee.gif")
        d = w.create_image(600, 300, image = lee)
    if "gaara" in playernames:
        gaara = PhotoImage(file = "gaara.gif")
        e = w.create_image(900, 300, image = gaara)
    #Turn cycle
    #Repeats until there is only one player still alive and active
    while len(players) != 1:
        #Runs for each alive player. and makes i the active player
        for i in players:
            #Debuffs all active buffs on defensive stats
            i.defensiveDebuff()
            #Updates the stats on each active player
            for j in players:
                statShow(j)
            w.update()
            repeat = True
            print("\n")
            print("%s's turn!" %(i.name))
            time.sleep(1)
            #Asks them what move they want to do and if they have enough chakra (energy) to do it
            while repeat == True:
                print("What do you want to do?")
                print(i.moves)
                move = raw_input()
                #Checks to see if they have enough chakra
                try:
                    if i.moves[move][1] <= i.chakra:
                        repeat = False
                    else:
                        print("Not enough chakra")
                except:
                    print("That is not a move")
            time.sleep(1)
            #Prints what move they used
            print("%s used %s!" % (i.name, move))
            #If the selected move is a damage type move runs associated code
            if i.moves[move][2] == "damage":
                repeat = True
                while repeat == True:
                    try:
                        print("Who do you want to attack?")
                        #Prints all the people that they can attack
                        for k in range(len(players)):
                            print(k,".", players[k].name)
                        #Gets the desired target
                        target = input()
                        if 0 <= target <= len(players) - 1:
                            repeat = False
                        else:
                            print("That is not an option.")
                    except:
                        print("Incorrect inputs")
                    
                #Random element that determines the success of attack and is used in the attack function. This is done outside of the function as when random was used in the seperate module with the function caused crashing
                rand = random.randint(0, 100 + (i.speed * i.speedMod))
                #Runs attack function
                i.attack(players[target], move, rand)
                #If the move knocks the target unconcious rids the target from the list of players and takes them out of the turn rotation
                if players[target].hp <= 0:
                    print("%s has been knocked unconcious! %d players remain!" %(players[target].name, len(players)-1))
                    for t in players:
                        statShow(t)
                    players.pop(target)
                #Debuffs all offensive buffs
                i.offensiveDebuff()
            #If the selected move is a rest type runs associated code
            elif i.moves[move][2] == "rest":
                i.chakra = i.chakra + 25
                print("%s rests... They gain more chakra" %(i.name))
            #Since the code is neither a damage nor rest type runs the buff code
            else:
                #Runs the buff function
                i.buff(players, move)
            #Increases their chakra level back up a bit
            i.chakra = i.chakra + 25
    return players

#Function that plays the music for the fighting
def fightMusic():
    return

#-------------------------------MAIN CODE-----------------------------
#Runs the intro and music 
Thread(target = introMusic).start()
Thread(target = intro).start()
#Sleeps to cause no overruns in the threading
time.sleep(10)
#Runs the character selection functions
Thread(target = selectMusic).start()
#Sets the returns of the function to the appropiate variables
players, playernames = characterSelect()
#Runs the fight and main code functions
Thread(target = fightMusic).start()
#Sets the return of the match function as the winner
winner = match(players, playernames)
#Writes out who won
print("THE WINNER IS %s!" %(winner[0].name))
time.sleep(1)
print("Thanks for playing!")
time.sleep(2)
