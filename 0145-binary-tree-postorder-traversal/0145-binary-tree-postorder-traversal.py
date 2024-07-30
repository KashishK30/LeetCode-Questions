# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(node, result):
            if not node:
                return 
            post_order(node.left, result)
            post_order(node.right, result)
            result.append(node.val)

        result = []
        post_order(root, result)
        return result