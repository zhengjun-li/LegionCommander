"""
Determine if a string has all unique characters without using DS
- only lowercase alphabet characters
O(n log n) using bit vector
"""

def is_unique(input: str):
    checker = 0
    for char in input:
        bit_digit = ord(char) - ord('a')
        if (checker & 1 << bit_digit) == 1:
            return False
        checker |= 1 << bit_digit
    return True

input = ""
result = is_unique(input)
print(result)
