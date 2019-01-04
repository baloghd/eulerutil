from typing import Iterable

def is_multiple_of_any(n: int, numbers: Iterable) -> bool:
    for num in numbers:
        if n % num == 0:
            return True
    return False

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True
            
