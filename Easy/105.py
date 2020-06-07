# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        mid_value = preorder[0]
        mid_inorder_index = inorder.index(mid_value)

        left_inorder = inorder[:mid_inorder_index]
        left_preorder = preorder[1:1 + mid_inorder_index]

        right_inorder = inorder[mid_inorder_index + 1:]
        right_preorder = preorder[1 + mid_inorder_index:]

        return TreeNode(mid_value, self.buildTree(left_preorder, left_inorder), self.buildTree(
            right_preorder, right_inorder)
        )
        