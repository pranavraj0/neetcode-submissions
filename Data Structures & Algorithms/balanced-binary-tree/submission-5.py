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
            
            # recurse to check balance of left and right
            left = balanced(root.left)
            right = balanced(root.right)

            # once you return from base case calculate height and balance and build up
            height = 1 + max(left[0], right[0])
            b = abs(left[0] - right[0]) <= 1 and left[1] and right[1]

            return height, b
        
        return balanced(root)[1]





