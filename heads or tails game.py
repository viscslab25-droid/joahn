# This Python code is a simple game where the player can choose between "HEADS" or "TAILS" and then a
# random result is generated. The player can win or lose points based on their choice. The game also
# includes a feature where the player can enter a "prestige shop" to buy upgrades like more luck, more
# points for winning, or points for losing.
import random
h=("heads","HEADS","Heads","h")
t=("tails","TAILS","Tails","t")
b=0
s=0
play=0
r=10**10
ra=0
ba=10**10
p_lvl=0
w_p=0
l_p=0
luck=0
    
while r>b:
    print("\U00002666 YOUR PRESTIGE LEVEL IS",p_lvl,"\U00002666")
    play+=1
    a=input("HEADS or TAILS\n")
    r1=random.randint(1,2)
    r2=random.randint(1+luck,100-luck)
    if r2==50:
        print("you hit the jackpot")
        b+=10**10
        s+=10**10
    elif a in h:
        if r1==1:
            print("you win")
            s+=1+w_p
        elif r1==2:
            print("you lose")
            s+=l_p
    elif a in t:
        if r1==1:
            print("you lose")
            s+=l_p
        elif r1==2:
            print("you win")
            s+=1+w_p
    v=input("Continue?(y/n)\n")
    if v=="y":
        b+=1
        continue
    elif v=="n":
        p=(s/play)*100
        print("your total points is:",s,"\nwin percentage=",p,"%")
    p_lvl+=1
    sh=input("would you like to enter the prestige shop?(y/n)[press 'q' to exit]\n")
    if sh=="y":
        print("what would you like to buy?\n")
        shop=int(input("1.more luck\n2.more points\n3.points for losing\n"))
        if shop==1:
            print("you gain more luck")
            luck+=1
            continue
        elif shop==2:
            print("you gain more points when winning")
            w_p+=1
            continue
        elif shop==3:
            print("you gain points even by losing")
            l_p+=1
            continue
    elif sh=="n":
        print("good luck in your nxt lvl")
    elif sh=="q":
        print("please play my game again :)")
        b+=1+r
    #find a way to implement prestige lvl and scores to be shown atlast
print("thank you for playing")
