n:int = 10**2
import random
# with open("dynamic.py","w") as f:
#     f.write("i:int = int(input('enter a number : '))\n")
#     for i in range(n+1):
#         if i%2 == 0:
#             state = "is even"
#         else:
#             state = "is odd"
#         f.write(f'if i == {i}:\n')
#         f.write(f'\tprint("{i} {state}")\n')
#     f.write("else:\n\tprint('The number was too large to comprhend')")
with open("iter.py","w") as f:
    for i in range(n+1):
        k:str = random.choice(["!","?","//","*",""])
        l:list[str] = []
        for j in range(i):
            l.append("1")
        f.write(f"#{k} {str(i):2s} => {"+".join(l)}\n")