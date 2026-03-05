'''a=int(input("enter startin value:"))
b=int(input("enter ending value:"))
c=int(input("enter sep value:"))
from random import randrange
import statistics as s
l=[]
for i in range(6):
    ran=randrange(a,b,c)
    l.append(ran)
    print(ran)
si=round(s.mean(l),3)
print(f"the mean of the numbers is{si}")
print(f"the mode of the numbers is{s.mode(l)}")
print(f"the median of the numbers is{s.median(l)}")
print(l)'''
def trap():
    a=b=0
    while True:
        if a==0:
            print(" "*9+"*")
        print((" "*(8-a)+"*")+(" "*(2+a+a)+"*"))
        a+=1
        if a==9:
            break
    a+=1
    while True:
        print((" "*(0+b)+"*")+(" "*(19-b-b)+"*"))
        b+=1
        a=a-1
        if a==0:
            print(" "*10+"*")
            break
import random
def r_sort(List:list):
    a=List.sort()
    l=[]
    for i in range(len(List)):
        r=random.randrange(len(list))
        l.append(List[r])
    return List
def cal(x:int|float,y:int|float,sym:str,both_val:bool=True):
    print("This is a calculator.")
    if sym=="+":
        s=x+y
        print(s)
        return s
    elif sym=="-":
        if both_val:
            s=x-y
            print(s)
            s1=y-x
            print(s1)
            return s,s1
        else:
            s=x-y
            print(s)
            return s
    elif sym=="*":
        s=x*y
        print(s)
        return s
    elif sym=="/":
        if both_val:
            s=x/y
            print(s)
            s1=y/x
            print(s1)
            return s,s1
        else:
            s=x/y
            print(s)
            return s
    else:
        print('bye wrld')
        return 0
import random

def sauce(main_tags: str, codes: str):
    d = {
        "a": [],
        "b": [],
        "c": [],
        "d": [],
        "e": []
    }
    if len(codes) != 6 or not codes.isdigit():
        print("Invalid codes")
        return d
    d[main_tags].append(codes)
    return d

# Create a single dictionary to collect all values
final_dict = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
    "e": []
}

for _ in range(10):
    r = str(random.randint(100000, 999999))  # convert to string for .isdigit() check
    a = random.choice(["a", "b", "c", "d", "e"])  # fixed this line
    result = sauce(a, r)
    
    # merge result into final_dict
    final_dict[a].extend(result[a])

print(final_dict)

