"""
Determine if a string is a permutation of a palindrome (can be rearranged into a palindrome)
Input: tact coa
Output: True, can be rearranged into taco cat, which is a plaindrome
Note:
- ignore spaces
- lowercase alphabet
O(n) time
O(m) space, m = alphabet size
How:
iterate through string and using bit vector, remember if each char appears an even
or odd number of times. If all even, then it can be made into a palindrome.
If all even and 1 odd, still can be made into palindrome.
"""

def check_permutation(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    counter1 = dict()
    counter2 = dict()
    for i in range(0, len(str1)): #O(n)
        if str1[i] in counter1: #O(1)
            counter1[str1[i]] += 1
        else:
            counter1[str1[i]] = 1

        if str2[i] in counter2:
            counter2[str2[i]] += 1
        else:
            counter2[str2[i]] = 1
    
    if counter1 == counter2: #O(m)
        return True
    else:
        return False

def palindrome_permutation(str1: str):
    str1 = str1.replace(" ", "")
    bit_vector = 0
    for ch in str1: #O(n)
        bit_digit = ord(ch) - ord('a')
        bit_vector ^= 1 << bit_digit #xor
    if bit_vector == 0: # all even number of chars, then it can be made into palindrome
        return True
    elif (bit_vector & (bit_vector-1) == 0): #cool bit manipulation to check if only 1 bit is 1: https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
        #check if power of 2 (has only 1 bit as 1, all others 0)
        #if power of 2 means it has all even number of chars except 1 is odd, still can be a palindrome
        return True
    else:
        return False

str1 = "tact coa"
result = palindrome_permutation(str1)
print(result)