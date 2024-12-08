def two_sets(n: int):
    target_sum = n * (n + 1) / 2
    if target_sum % 2 != 0:
        return ("NO", [], [])

    set_1 = []
    set_2 = []

    target_sum //= 2
    for i in range(n, 0, -1):
        if i <= target_sum:
            set_1.append(i)
            target_sum -= i
        else:
            set_2.append(i)

    return ("YES", set_1, set_2) if target_sum == 0 else ("NO", [], [])


if __name__ == "__main__":
    n = int(input())

    result = two_sets(n)
    print(result[0])
    if result[0] == "YES":
        print(len(result[1]))
        print(*result[1])
        print(len(result[2]))
        print(*result[2])