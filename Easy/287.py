class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while(slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow