"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Greedy solution that iterates through array via jumping, choosing the best place to jump each time. 
"""
class Solution(object):
    jumps = 0
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        return self.chooseJump(nums, 0)
        
    def chooseJump(self, nums, current):
        jumpLength = nums[current]
        if jumpLength + current + 1 >= len(nums):
            return self.jumps + 1
        max = 0
        next = current
        for x in range(current + 1, jumpLength + current + 1):
            temp = nums[x] - (jumpLength + current - x)
            if temp > max:
                max = temp
                next = x
        self.jumps += 1

        return self.chooseJump(nums, next)
    
input()
variable = Solution()
array = [1, 3, 2]
print(variable.jump(array))                