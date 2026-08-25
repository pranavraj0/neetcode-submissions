# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        


        def pathSum(root, currentSum):
            if not root:
                return False

            # add current node to currentSum
            currentSum += root.val

            if not root.left and not root.right:
                return currentSum == targetSum

            return pathSum(root.left, currentSum) or pathSum(root.right, currentSum)

        return pathSum(root, 0)