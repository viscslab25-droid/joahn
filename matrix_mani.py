import time
import random
import os


l:list[list[str]] = []

def randomise(rx:int,ry:int):    
    for x in range(8):
        t:list[str] = []
        for y in range(8):
            if (x,y) == (rx,ry):
                t.append(f"#")
            else:
                t.append("*")
        l.append(t)
    return l

def render(chunk:list[list[str]]) -> None:
    for row in chunk:
        print("".join(row))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

for _ in range(10):
    rx = random.randint(0,7)
    ry = random.randint(0,7)

    clear()                     # 1️⃣ clear first
    render(randomise(rx, ry))   # 2️⃣ draw frame
    time.sleep(1/10)            # 3️⃣ wait