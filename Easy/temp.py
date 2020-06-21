class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.recurse(nums, 0)
        
    def recurse(self, nums, index):
        range = nums[index]

        #base case
        if range + index >= len(nums):
            return 1

        #recursive case
        max = 0
        maxIndex = 0
        for i in range(index + 1, range + 1):
            if (nums[i] - (range - i)) > max:
                max = nums[i]
                maxIndex = i
        return 1 + self.recurse(nums, maxIndex)
        
        