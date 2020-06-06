/**
 * recursion to count max depth of tree. has to visit every node
 * bigO = n
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root->left == NULL && root->right == NULL)
        {
            return 1;
        }
        if(root->left == NULL && root->right != NULL)
        {
            return maxDepth(root->right) + 1;
        }
        if(root->left != NULL && root->right == NULL)
        {
            return maxDepth(root->left) + 1;
        }
        if(root->left != NULL && root->right != NULL)
        {
            int leftDepth = maxDepth(root->left);
            int rightDepht = maxDepth(root->right);
            if(leftDepth >= rightDepht)
            {
                return leftDepth + 1;
            } else
            {
                return rightDepht + 1;
            }
            
        }
        return 0;
    }
};
