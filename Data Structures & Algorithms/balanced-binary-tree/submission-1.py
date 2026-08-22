# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursively compare heights of both subtrees?
        def height(root):
            if not root:
                return 0

            
            leftHeight = 1 + height(root.left)
            rightHeight = 1 + height(root.right)
            return max(leftHeight, rightHeight)

        def balanced(root):
            if not root:
                return True
            # where does height come in? 
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight) <= 1:
                return balanced(root.left) and balanced(root.right)
            else:
                return False

        return balanced(root)