# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(root):
            if not root:
                return 0,True
            
            left = balanced(root.left)
            right = balanced(root.right)

            height = 1 + max(left[0], right[0])
            b = True if abs(left[0] - right[0]) <= 1 and left[1] == True and right[1] == True else False

            return height, b
        
        return balanced(root)[1]





