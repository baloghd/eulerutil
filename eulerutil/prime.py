from typing import Iterable, List
from collections import Counter

#from eulerutil.number_theory import divides

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True
            
def sieve(limit: int) -> List[int]:
    table = {}
    
    for i in range(2, limit + 2):
        table[i] = True
    
    q = 2
    while q <= limit:
        if table[q] == True:
            mult = q * q
            while mult <= limit:
                table[mult] = False
                mult += q
        q += 1
        
    tofilter = [i if table[i] == True else None for i in range(2, limit)]
    
    return list(filter(lambda x: x is not None, tofilter))

#def prime_factors(n: int) -> Counter:
    #p = sieve(n)
    #factors = []
    #while n >= 1:
        #for prime in p:
            #if n % prime == 0:
                #factors.append(prime)
                #n /= prime
                #break
    #return Counter(factors)
    
def prime_factors(n: int) -> Counter:
    if is_prime(n):
        return Counter([n])
    p = sieve(n)
    t = n
    factors = []
    while n > 1:
        for prime in p:
            if n % prime == 0:
                factors.append(prime)
                n /= prime
                break
    return Counter(factors)

def consolidate_prime_factors(c: Counter) -> List[int]:
    cons = []
    for k in c.keys():
        cons.append(k**c[k])
    return cons


from random import randrange

# etc.

def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    small_primes = sieve(1000)
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


#def is_primeMR(n: int, k: int) -> bool:
    #"""Miller-Rabin primality test"""
    #assert(n > 3)
    
