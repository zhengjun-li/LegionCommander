"""
This is solved using a segment tree:
binary
full (all but last level is filled)
leaf nodes represent element
internal nodes represent sum of left and right children

To build a segment tree is very simple recursively:
1. create parent node
2. create and attach left and right children node
3. sum children values and update parent node

base case:

1. When left and right iterators cross
    return None
2. When left and right iterators equal:
    create leaf node and return

iterative case:
"we are building tree for interval [l, r]"
its children are trees of interval [l, m] and [m + 1, r]
where b is the mid point


"""

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):

    internal_list = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def createTree(nums, l, r):

            if l > r:
                return None
            
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2

            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)

            root.total = root.left.total + root.right.total

            return root
        
        self.root = createTree(nums, 0, len(nums) - 1)
        

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