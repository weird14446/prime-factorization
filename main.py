from typing import List
from functools import reduce


def prime_list(n: int):
    sieve: List[bool] = [True] * n

    m: int = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


def primeFactorization(n: int) -> List[int]:
    num: int = n
    arr: List[int] = prime_list(n)
    ret: List[int] = []
    i: int = 0
    while num != 1:
        if num % arr[i] == 0:
            num //= arr[i]
            ret.append(arr[i])
        else:
            i += 1
    return ret


if __name__ == "__main__":
    n: int = int(input())
    arr: List[int] = primeFactorization(n)
    print(arr)
    print(reduce(lambda x, y: x * y, arr))
