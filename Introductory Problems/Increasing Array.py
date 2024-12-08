def increasing_array(n: int, a: list) -> int:
    modify_count = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            modify_count += a[i - 1] - a[i]
            a[i] = a[i - 1]
    return modify_count

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(increasing_array(n, a))