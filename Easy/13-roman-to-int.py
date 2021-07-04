# Ask for forgiveness approach. First, turn roman numeral into int,
# and then see if next roman numeral is combinable
import math
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prevVal = math.inf
        for char in s:
            currVal = self.getIntValue(char)
            
            if currVal > prevVal:
                total = total + currVal - (prevVal * 2)
            else:
                total += currVal
            prevVal = currVal
        return total
                
    def getIntValue(self, ch) -> int:
        if ch == 'I':
            return 1
        elif ch == 'V':
            return 5
        elif ch == 'X':
            return 10
        elif ch == 'L':
            return 50
        elif ch == 'C':
            return 100
        elif ch == 'D':
            return 500
        elif ch == 'M':
            return 1000
        else:
            return None
        
            