"""
Compress given string "aaabbbbcc" into "a3b4c2", return original str if compressed is not shorter
- lowercase a-z only
"""
def compress_string(str1: str):
    compressed_str = []
    seq_start = 0 #inclusive
    for i in range(len(str1)):
        if i == len(str1) - 1 or str1[i] != str1[i+1]:
            count = i + 1 - seq_start
            compressed_str.append(str1[i] + str(count))
            seq_start = i + 1
    if len(compressed_str) < len(str1):
        return "".join(compressed_str)
    else:
        return str1

input = "aabcccccaaa"
result = compress_string(input)
print(result)