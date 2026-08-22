# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursively compare heights of both subtrees?
        balanced_mapping = {}
        def height(root):
            if not root:
                return 0

            leftHeight = 1 + height(root.left)
            rightHeight = 1 + height(root.right)
            balanced_mapping[root] = True if abs(leftHeight - rightHeight) <= 1 else False
            return max(leftHeight, rightHeight)

        height(root)

        for i in balanced_mapping.values():
            if not i:
                return False
        return True
        