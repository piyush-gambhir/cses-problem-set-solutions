import sys
from typing import List


def weird_algorithm(n: int) -> List[int]:
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res.append(n)
    return res


if __name__ == "__main__":
    input = sys.stdin.read
    i = int(input().strip())
    print(*weird_algorithm(i))
