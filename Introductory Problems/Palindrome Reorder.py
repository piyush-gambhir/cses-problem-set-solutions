def palindrome_reorder(input_string: str) -> str | None:
    alphabet_count = {}
    for alphabet in input_string:
        if alphabet in alphabet_count:
            alphabet_count[alphabet] += 1
        else:
            alphabet_count[alphabet] = 1

    if (len(input_string) % 2 == 0):
        