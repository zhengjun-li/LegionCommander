"""
Determine if 2 strings are permutations of each other
O(n) time and O(m) space for hash table of alphabet size
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


str1 = "fdsafdsafdsa"
str2 = "asdfasdfasdf"
result = check_permutation(str1, str2)
print(result)