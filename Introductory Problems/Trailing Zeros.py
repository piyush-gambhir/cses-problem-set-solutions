def tailing_zero(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

if __name__ == "__main__":
    n = int(input())
    print(tailing_zero(n))