import random, winsound, threading, time, Fighters
from Tkinter import *
from threading import Thread
master = Tk()
w = Canvas(master, width = 1000, height = 600, bg = "white")
w.pack()
title = PhotoImage(file = "title.gif")
select = PhotoImage(file = "select.gif")
fight = PhotoImage(file = "setting.gif")
def intro():
    a = w.create_image(500, 300, image = title)
    w.update()
    print "WELCOME TO THE NARUTO FIGHTING ARENA"
    time.sleep(1)
    print
    print "Instructions:"
    print "1. You can have 2-4 players at a time"
    time.sleep(1)
    print "2. Defensive buffs (things that buff defense or sharingan) last only one turn cycle"
    time.sleep(1)
    print "3. Offensive buffs (moves that buff speed or attack) last until you attack"
    time.sleep(1)
    print "4. When calling on a move. Write exactly what the move is listed as"
    time.sleep(1)
    print "5. Do not close the Tkinter windows"
    time.sleep(1)
    print "6. You can only play one of each character"
    time.sleep(1)
    print "7. For information on your characters health, chakra, etc. look to Tkinter window"
    time.sleep(1)
    print "8. Do not worry if your stats on the Tkinter window do not change after a buff. The buffs only are taken into account when needed."
    time.sleep(1)
    print "9. Sharingan will only copy one move per activation"
    time.sleep(1)
    w.delete(a)
    mainloop()
    
def introMusic():
    winsound.PlaySound("opening.wav", winsound.SND_FILENAME)
    
def characterSelect():
    a = w.create_image(400,300, image = select)
    w.update()
    repeat = True
    players = []
    playernames = []
    print
    print "How many players? MAX 4 / MIN 2"
    participants = input()
    for i in range(participants):
        repeat = True
        while repeat == True:
            print "PLAYER NUMBER", i + 1
            print "Who do you want to play as? Rock Lee? Naruto Uzamaki? Sasuke Uchiha? Gaara of the Sand?"
            x = raw_input().lower()
            if x == "lee" and "lee" not in playernames or x == "rock lee" and "lee" not in playernames:
                i = Fighters.fighter("Rock Lee", 150, 100, 150, 200)
                playernames.append("lee")
                repeat = False
            elif x == "naruto" and "naruto" not in playernames or x == "naruto uzamaki" and "naruto" not in playernames:
                i = Fighters.fighter("Naruto Uzamaki", 250, 100, 100, 150)
                playernames.append("naruto")
                repeat = False
            elif x == "sasuke" and "sasuke" not in playernames or x == "sasuke uchiha" and "sasuke" not in playernames:
                i = Fighters.fighter("Sasuke Uchiha", 200, 150, 100, 150)
                playernames.append("sasuke")
                repeat = False
            elif x == "gaara" and "gaara" not in playernames or x == "gaara of the sand" and "gaara" not in playernames:
                i = Fighters.fighter("Gaara of the Sand", 100, 200, 150, 100)
                playernames.append("gaara")
                repeat = False
            else:
                print "That is not an option. Sorry."
        players.append(i)
    return players, playernames

def statShow(player):
    if player.name == "Naruto Uzamaki":
        j = w.create_rectangle(10,10,210,110, fill = "white", outline = "black")
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
    w.update()

def selectMusic():
    winsound.PlaySound("select.wav", winsound.SND_FILENAME)

def match(players, playernames):
    a = w.create_image(500,300, image = fight)
    w.update()
    if "naruto" in playernames:
        naruto = PhotoImage(file = "naruto.gif")
        b = w.create_image(100, 300, image = naruto)
        j = w.create_rectangle(10,10,210,110, fill = "white", outline = "black")
    if "sasuke" in playernames:
        sasuke = PhotoImage(file = "sasuke.gif")
        c = w.create_image(360, 300, image = sasuke)
        k = w.create_rectangle(260,10,460,110, fill = "white", outline = "black")
    if "lee" in playernames:
        lee = PhotoImage(file = "lee.gif")
        d = w.create_image(600, 300, image = lee)
        l = w.create_rectangle(510,10,710,110, fill = "white", outline = "black")
    if "gaara" in playernames:
        gaara = PhotoImage(file = "gaara.gif")
        e = w.create_image(900, 300, image = gaara)
        k = w.create_rectangle(760,10,960,110, fill = "white", outline = "black")
    
    while len(players) != 1:
        for i in players:
            i.defensiveDebuff()
            w.update()
            for j in players:
                statShow(j)
            repeat = True
            print
            print "%s's turn!" %(i.name)
            time.sleep(1)            
            while repeat == True:
                print "What do you want to do?"
                print i.moves
                move = raw_input()
                if i.moves[move][1] < i.chakra:
                    repeat = False
                else:
                    print "Not enough chakra"
            time.sleep(1)
            print "%s used %s!" % (i.name, move)
            if i.moves[move][2] == "damage":
                print "Who do you want to attack?"
                possTargets = players
                possTargets.remove(i)
                for k in range(len(possTargets)):
                    print k,".", possTargets[k].name
                target = input()
                rand = random.randint(0, 100 + (i.speed * i.speedMod))
                i.attack(players[target], move, rand)
                if players[target].hp <= 0:
                    print "%s has been knocked unconcious! %d players remain!" %(players[target].name, len(players)-1)                    
                    players.remove(players[target])
                i.offensiveDebuff()
            else:
                i.buff(players, move, i.moves[move][3], i.moves[move][0])

def fightMusic():
    winsound.PlaySound("Fight Music-0.wav", winsound.SND_FILENAME)
    winsound.PlaySound("Fight Music-1.wav", winsound.SND_FILENAME)

#-------------------------------MAIN CODE-----------------------------
Thread(target = introMusic).start()
Thread(target = intro).start()
time.sleep(10)
Thread(target = selectMusic).start()
players, playernames = characterSelect()
Thread(target = fightMusic).start()
winner = match(players, playernames)
print "THE WINNER IS %S!" %(winner[0].name)
time.sleep(1)
print "Thanks for playing!"
time.sleep(2)
