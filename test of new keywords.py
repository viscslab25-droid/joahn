import random
h=("heads","HEADS","Heads")
t=("tails","TAILS","Tails")
b=0
s=0
play=0
r=10**10
while r>b:
    play+=1
    a=input("HEADS or TAILS\n")
    r1=random.randint(1,2)
    if a in h:
        if r1==1:
            print("you win")
            s+=1
        elif r1==2:
            print("you lose")
    elif a in t:
        if r1==1:
            print("you lose")
        elif r1==2:
            print("you win")
            s+=1
    v=input("Continue?(y/n)\n")
    if v=="y":
        b+=1
    elif v=="n":
        b+=10**10
p=(s/play)*100
print("your total points is:",s,"\nwin percentage=",p,"%")
            
