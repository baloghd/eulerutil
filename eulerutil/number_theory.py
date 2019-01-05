from typing import Tuple, Set, List

def even(n: int) -> bool:
    return n % 2 == 0

def odd(n: int) -> bool:
    return not even(n)

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

def divides(a: int, b: int) -> bool:
    return b % a == 0

def Collatz_sequence(n: int) -> List[int]:
    seq = []
    t = n
    while n != 1:
        seq.append(str(int(n)))
        if even(n):
            n /= 2
        else:
            n = 3*n + 1
    seq.append(1)
    return dict(zip(seq, [i for i in range(len(seq) - 1, 0, -1)]))
