'''
O(N)
However, question wanted O(logN) solution. Idk how to get that yet
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[1] < nums[0]:
            return 0
        else:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return i
            return len(nums) - 1
         