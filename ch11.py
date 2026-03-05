def len_c(w1:str="PANDA",w2:str="Python"):
    a=len(w1)
    b=len(w2)
    c=0
    if a>b:
        if a%2==1:
            c=1
        for i in range(a//2):
            print(" "*(i)+w1[0+i]+" "*(a-(i*2))+w1[-1-i])
            if c==1:
                print(" "*(i+2)+w1[a//2])
    elif b>a:
        if b%2==1:
            c=1
        for i in range(b//2):
            print(" "*(i)+w2[0+i]+" "*(b-(i*2))+w2[-1-i])
            if c==1:
                print(" "*(i+2)+w2[b//2])
import math
import time
import os

def fac(x: int)->int:
    if x in (0, 1):
        return 1
    return fac(x - 1) * x

max_fac = fac(50)
bar_length = 50

for x in range(51):
    current = fac(x)
    
    # Compute logarithmic progress
    log_progress = math.log(current + 1) / math.log(max_fac + 1)
    
    filled = int(bar_length * log_progress)
    bar = "|" + "=" * filled + " " * (bar_length - filled) + "|"
    
    # Clear the screen each iteration (optional)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"Computing factorials... {x}/50")
    print("_" * (bar_length + 1))
    print(f"{bar} {log_progress * 100:6.2f}%")
    print("-" * (bar_length + 1))
    
    # Optional: show current factorial (comment this out if too long)
    # print(f"{x}! = {current}")
    
    # Small pause for animation
    time.sleep(0.1)

print("\n✅ All factorials computed!")
