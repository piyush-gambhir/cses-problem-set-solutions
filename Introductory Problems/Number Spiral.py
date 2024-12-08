def find_spiral_value(x, y):
    if x > y:
        if x % 2 == 0:
            return x * x - y + 1
        else:
            return (x - 1) * (x - 1) + y
    else:
        if y % 2 == 0:
            return (y - 1) * (y - 1) + x
        else:
            return y * y - x + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(find_spiral_value(x, y))
