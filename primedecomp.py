# function for printing the prime factorization of a number n > 1

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
