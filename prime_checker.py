from math import sqrt
import time
t = time.time()


def prime_checker(x: int) -> bool:
    if x % 2 == 0 and x != 2: return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x % i == 0: return False
    return True


def sieve(n: int):
    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, n, i):
                primes[multiple] = False

    return [i for i in range(n) if primes[i]]


def sieve_byte(n: int):
    primes = bytearray(b'\x01') * n
    primes[0:2] = b'\x00\x00'

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i:n:i] = b'\x00' * len(primes[i*i:n:i])

    return [i for i in range(n) if primes[i]]
# Minecraft@2025

fin = sieve_byte(10**7)

print(time.time()-t)

fin = sieve(10**6)

print(time.time() - t)

fin = [x for x in range(10**6) if prime_checker(x=x)]

print(time.time()-t)
