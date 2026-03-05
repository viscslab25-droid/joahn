print("You are playing the game. Press the ENTER key to start")
import sys
import random
import time
#remeber max limit should be 2^32
r = random.randint(1,20)#for dmg
ra= random.randint(1,20)#for mana
ran= random.randint(1,20)#for hp
rand=random.randint(1,20)#for attack spped
R = random.randint(1,100)#for general
admin_pwrs= ["johan","irene","admin"]
alpha_testers=["sonish","hema","dk"]
gold=10+(r//2)
exp=1
hp=10
admin=1
test=1
lvl=0
input()
print("Hello there  adventurer, what is your name?")  
a=input("Choose your character's name:")
print ("you have gained exp")
if a in admin_pwrs:
    input()
    print("You have unlocked admin powers")
    input()
    print("your dmg and exp are maxed for a lvl 10 player")
    admin=2**10
elif a in alpha_testers:
        print("you have gained 'playtester' title")
        print(a," huh what  an interesting name there")
        test=(1.1**R)
else:
        print(a," huh what  an interesting name there")
input()
print("now , where are you going adventurer?")
print("press 1 for going toward the river \n press 2 for going to the loud noises")
b=int(input("choose your path="))
if b>2:
    print('''you have died , better luck next time  '.----.'   ''')
    sys.exit()
else:
    print("you move in that direction")
    input()
    print("you encounter a dragon.")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    input()
    b=int(input(" \n type 1 to run into  a dungeon \n type 2 to run into a forest:"))
if b>1:
    print('you have entered the forset')
    input()
    print("you have encounterred a monster")
    c=int(input("1.run , 2.fight"))
    if c==1:
        print("You have succesfullly fled the MONSTER ")
        print('current exp =',exp-1)
    else :
        m_hp=10
        dmg=2*admin*test
        t_dmg=r*dmg
        print("monster's hp =",m_hp)
        print("your dmg is",t_dmg)
        if t_dmg>=10:
            int()
            print("you have succesfully defeated the monster")
            print("would you like to loot it?")
            a=int(input("1.yes 2.no"))
            if a==1:
                loot=10*R
                print("you have obtained the CORE OF THE BEAST(D-)")
                inv="CORE OF THE BEAST(D-)"
            else:
                      print("the corpse has withered away")
            exp=exp+1
        else:
            print("YOU HAVE DIED")
            input()
            sys.exit()
            print("\t\t\tEND SCREEN")
            print("your current hp =",hp*admin)
            print("your current exp =",exp*admin)
            print("your current gold =",gold*admin,"\U0001FA99")
            print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")
            
else:
    print("you have entered the dungeon")
    input()
    print("you encounter a fork in the path")
    a=int(input("1. left \n 2.right"))
#think of beter ways to implement color and othertxt effects 
#ris the random numnber generator tht determines combat
#implement r into combat
#implement attack speed into combat
#implement mana and hp into cmbat
if hp<0:
    print("\tYOU HAVE DIED")
    input()
    sys.exit()
print("\t\t\tEND SCREEN")
print("your current hp =",hp*admin)
print("your current exp =",exp*admin)
print("your current gold =",gold*admin,"\U0001FA99")
print("your luck = "+str(r),ra,ran,rand,R,sep="\U00002694")

  
