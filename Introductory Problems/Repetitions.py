def longest_repetition(s: str) -> int:
    max_length = 0
    current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)  

if __name__ == "__main__":
    s = input().strip()
    print(longest_repetition(s))
