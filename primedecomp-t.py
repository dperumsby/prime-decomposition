#!/usr/bin/env python3

# function for printing the prime factorization of a number n > 1
# syntax: primef <number>

import sys

try:
    n = int(sys.argv[1])
except:
    print("primef calculates the prime factorization of a number")
    print("Please use the syntax: primef <number>")
    sys.exit()


def primef(n):
    decomp = ""
    d = 2
    while n > 1:
        counter = 0
        while n % d == 0:
            n //= d
            counter += 1
        if counter > 0:
            decomp += f"({d}**{counter})" if counter > 1 else f"({d})"
        d += 1
        if d*d > n:
            if n > 1: decomp += f"({n})"
            break

    return decomp 


print(primef(n))
