# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        while root and root.left:
            root = root.left
        return root.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # at the node to delete
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            minVal = self.minNode(root.right)
            print(minVal, root.val)
            root.val = minVal
            root.right = self.deleteNode(root.right, minVal)

        return root
            # there is a left and right child
