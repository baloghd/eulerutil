from typing import Iterable
from eulerutil.number_theory import gcd

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True
            
#def Pollards_rho(n: int) -> bool or int:
    #g_x = lambda x: (x**2 + 1) % n
    #x, y = 2, 2
    #d = 1
    #while d == 1:
        #x = g_x(x)
        #y = g_x(g_x(y))
        #d = gcd(abs(x - y), n)
    #if d == n:
        #return False
    #else:
        #return d
