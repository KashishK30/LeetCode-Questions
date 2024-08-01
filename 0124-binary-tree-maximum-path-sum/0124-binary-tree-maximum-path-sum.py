# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(node):
            nonlocal max_sum
            if not node:
                return 0


            left = max(maxSum(node.left), 0)
            right = max(maxSum(node.right), 0)

            current_sum = left + node.val + right

            max_sum = max(max_sum,current_sum)

            return node.val + max(left, right)

        max_sum = float('-inf')
        maxSum(root)
        return max_sum