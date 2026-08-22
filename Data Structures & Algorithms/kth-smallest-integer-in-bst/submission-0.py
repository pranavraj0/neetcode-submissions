# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        curr = 0
        val = 0
        def kthRecursive(root):
            nonlocal curr
            nonlocal val
            if not root:
                return
            
            kthRecursive(root.left)
            curr +=1
            if curr == k:
                val = root.val
            kthRecursive(root.right)
             

        kthRecursive(root)
        return val
