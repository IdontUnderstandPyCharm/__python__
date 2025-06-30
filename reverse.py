def reverse_str(s, k):
    s = list(s)
    print(s, len(s))
    for i in range(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)

print(reverse_str("abcdefg", 2))  # "bacdfeg"
print(reverse_str("abcd", 2))     # "bacd"
