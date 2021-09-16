"""
Climbing Stairs
O(n) time
O(n) space

Dynamic Programming
waysToClimb[i]: number of ways to get to top from ith step
calc waysToClimb[n - 1], then recurse down to 0

Could have done this in a for loop lol

"""

class Solution:
    waysToClimb = []
    def getNumberOfWays(self, i, n):
        if i == n - 1:
            self.waysToClimb[i] = 1
        else:
            self.getNumberOfWays(i + 1, n)
            self.waysToClimb[i] = self.waysToClimb[i+1] + self.waysToClimb[i+2]
    
    def climbStairs(self, n: int) -> int:
        #waysToClimb[i]: number of ways to climb to top from ith step
        self.waysToClimb = [1 for i in range(n + 1)]
        self.getNumberOfWays(0, n)
        return self.waysToClimb[0]