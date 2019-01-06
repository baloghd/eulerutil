from typing import Tuple, Set, List
import math

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

def digits(n: int) -> List[int]:
    d = []
    while n >= 1:
        d.append(n % 10)
        n //= 10
    return d

def numdigits(n: int) -> int:
    return math.floor(math.log10(n)) + 1
    
def sumdigits(n: int) -> int:
    d = 0
    while n >= 1:
        d += n % 10
        n //= 10
    return d

def divides(a: int, b: int) -> bool:
    return b % a == 0

def is_square(n: int) -> bool:
    if (n < 0):
        return False
    root = math.sqrt(n) + 0.5
    return root * root == n

def Fibonacci(n: int) -> int:
    lookup = {1: 1, 2: 1}
    def fib(n):
        if n <= 2:
            return 1
        if n in lookup:
            return lookup[n]
        else:
            lookup[n] = fib(n-1) + fib(n-2)
            return lookup[n]
    return fib(n)

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

