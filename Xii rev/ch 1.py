import math,random

def prime(n):
    if n < 2 or n % 2 == 0 and n != 2:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
def minutes(t):
    return f"{t//60} minutes, {t%60} seconds"
def table(r,c):
    for m in range(1,r+1):
        for n in range(1,c+1):
            prod = m*n
            if prod < 10:
                print(f" {prod} ",end = " ")
            else:
                print(f"{prod} ",end = " ")
        print()
def day_guesser(day_1,n):
    day_dic = {
        "Sun":0,
        "Mon":1,
        "Tue":2,
        "Wed":3,
        "Thu":4,
        "Fri":5,
        "Sat":6
    }
    return (day_dic[day_1]+n-1)%7
def sum(n:int):
    c = 0
    if n > 0:
        for i in range(n,2*n+1):
            c += i
    else:
        for i in range(2*n,n+1):
            c += i
    return c
print(sum((-5)))