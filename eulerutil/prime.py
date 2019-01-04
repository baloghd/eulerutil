from typing import Iterable

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True
            
