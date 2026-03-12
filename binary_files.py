def collatz_conjecture(n:int)->str:
    # if n <= 0:
    #     raise ValueError("n must be a positive integer")
    if 1 == n:
        return "->1"
    elif n%2==0:
        return f"->{n}{collatz_conjecture(n//2)}"
    else:
        return f"->{n}{collatz_conjecture(3*n+1)}"
with open("collatz_conjecture.txt", "w") as f:
    for i in range(1, 101):
        f.write(collatz_conjecture(i) + "\n\n")

def neg_collatz(x: int) -> str:
    z = x
    visited:set[int] = set()
    final = f"->{x}"

    while z not in visited:
        visited.add(z)

        if z % 2 == 0:
            z = z // 2
        else:
            z = 3*z + 1

        final += f"->{z}"

        if z == x:
            return final

    return final
with open("neg_collatz.txt", "w") as f:
    for i in range(-1, -101, -1):
        f.write(neg_collatz(i) + "\n\n")

def collatz_conjecture_v2(first:int,mul:int=3,add:int=1,div:int=2)->set[int]:
    seen:set[int] = set()
    x = first
    while x not in seen:
        seen.add(x)
        if x%2==0:
            seen.add(x//div)
        else:
            seen.add(mul*x+add)
        if x == first:
            return seen
    return set()
with open("collatz_conjecture_v2.txt", "w") as fin:
    for f in range(1,6):
        for m in range(6):
            for a in range(6):
                for d in range(1,6):
                    fin.write(f"first={f}, mul={m}, add={a}, div={d} -> {collatz_conjecture_v2(f,m,a,d)}\n\n")