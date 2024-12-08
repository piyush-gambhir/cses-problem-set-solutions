def permutations(n):
    if n == 1:
        return [1]
    if n == 2 or n == 3:
        return None

    result = []
    for i in range(2, n + 1, 2):
        result.append(i)

    for i in range(1, n + 1, 2):
        result.append(i)

    return result


if __name__ == "__main__":
    n = int(input())
    result = permutations(n)
    if result is None:
        print("NO SOLUTION")
    else:
        print(" ".join(map(str, result)))
