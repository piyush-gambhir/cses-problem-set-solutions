def bit_strings(n: int) -> int:
    modulo = 10**9 + 7
    bit_strings = 2**n
    return bit_strings % modulo

if __name__ == "__main__":
    n = int(input())
    print(bit_strings(n))