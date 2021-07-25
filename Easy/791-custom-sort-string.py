'''
O(mn)
m = len(order)
n = len(s)
this all depends on O(s.replace())
if it is O(N), then solution is O(mn)
TODO: figure out exactly what this runtime is
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        newString = ''
        for char in order:
            oldLength = len(s)
            s = s.replace(char, '')
            for i in range(oldLength - len(s)):
                newString += char
        newString += s
        return newString