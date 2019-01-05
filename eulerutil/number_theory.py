from typing import Tuple, Set

def gcd(a: int, b: int) -> int:
    while b > 0:
        t = b
        b = a % b
        a = t
    return a

def numdivisors(n: int, div_list = False) -> int or Tuple[int, Set]:
    i = 1
    nd = 1
    if div_list:
        dl = {n}
    while 2*i <= n:
        if n % i == 0:
            nd += 1
            if div_list:
                dl.add(i)
        i += 1
    if div_list:
        return nd, dl
    return nd

def numdigits(n: int) -> int:
    d = 0
    while n >= 1:
        d += 1
        n /= 10
    return d

def sumdigits(n: int) -> int:
    d = 0
    while n >= 1:
        d += n % 10
        n //= 10
    return d
