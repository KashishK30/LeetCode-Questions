# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def in_order_traversal(node):
            if node:
                yield from in_order_traversal(node.left)
                yield node.val
                yield from in_order_traversal(node.right)
            
        seen = set()
        for value in in_order_traversal(root):
            if (k - value) in seen:
                return True
            seen.add(value)
        return False
            
            