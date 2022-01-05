"""
Determine if two strings are one edit away. Edits are: insert char, remove char, replace char.
- remove and insert are actually the same. If you can remove 1 char from input to make it same as input2,
    you can also insert 1 char into input2 for the same result

O(n log n) using bit vector
"""

#can you replace 1 char in str1 to match it with str2
def check_replace(str1: str, str2: str):
    differences = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differences += 1
            if differences > 1:
                return False
    return True

#can you remove 1 char from str1, or insert 1 char into str2 to make them the same?
#len(str1) == len(str2) + 1
def check_remove_insert(str1: str, str2: str):
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            #"pretend" to insert or remove 1 char and continue comparisons
            str3 = str1[i+1:]
            str4 = str2[i:]
            if str3 == str4:
                return True
            else:
                return False
    return True

def one_away(input: str, input2: str):
    if len(input) == len(input2):
        return check_replace(input, input2)
    elif len(input) + 1 == len(input2):
        return check_remove_insert(input, input2)
    elif len(input) - 1 == len(input2):
        return check_remove_insert(input2, input)
    else:
        return False


    

input = ""
input2 = ""
result = one_away(input)
print(result)