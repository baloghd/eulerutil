from typing import List

def factorial(n: int) -> int:
    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1


def Pascal_triangle(row: int) -> List[int]:
    line = [1]
    for k in range(row):
        line.append(line[k] * (row - k) / (k + 1))
        print(line)
    return line


def choose(n: int, k: int) -> int:
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

