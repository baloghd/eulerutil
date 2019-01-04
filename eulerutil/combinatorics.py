from typing import List
from functools import reduce

def factorial(n: int) -> int:
    if n >= 1:
        return n * rec_factorial(n - 1)
    else:
        return 1


def choose(n: int, k: int) -> int:
    return factorial(n) / (factorial(k) * factorial(n - k))

