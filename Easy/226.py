'''
Invert a binary tree

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    newRoot = TreeNode()
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        #inverse right side and add to left
        newLeft = self.invertTree(root.right)

        #inverse left side and add to right
        newRight = self.invertTree(root.left)

        root.left = newLeft
        root.right = newRight

        return root

'''
1. Traverse tree:
- center, right, left
2. Build tree center, left, right
'''