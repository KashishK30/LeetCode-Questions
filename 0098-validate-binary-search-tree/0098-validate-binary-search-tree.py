# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalidBST(node, low = -float('inf'), upper = float('inf')):
            if not node:
                return True

            if not (low < node.val < upper):
                return False

            return isvalidBST(node.left, low, node.val) and isvalidBST(node.right, node.val, upper)
        return isvalidBST(root)