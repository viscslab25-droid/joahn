import time
import random
def shift(t: list[int], n: int) -> list[int]:
    return t[n:]+t[:n]
a:list[int] = list(range(25))
i = 0
while True:
    random.shuffle(a)
    print(shift(a, i%10),end="\r")
    i+=1
    time.sleep(1/24) 