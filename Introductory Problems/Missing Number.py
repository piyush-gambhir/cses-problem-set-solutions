import sys


def find_missing_number(n, numbers):
    total_sum = n * (n + 1) / 2
    actual_sum = sum(numbers)
    return int(total_sum - actual_sum)


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    numbers = list(map(int, data[1:]))

    print(find_missing_number(n, numbers))
