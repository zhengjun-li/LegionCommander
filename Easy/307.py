class NumArray(object):

    internal_list = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.internal_list = nums
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.internal_list[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        total = 0
        for k in range(i, j + 1):
            total += self.internal_list[k]
        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)