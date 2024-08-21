# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0

        def post_order(node):
            if not node:
                return  True, 0, float('inf'), float('-inf')
            
            left_subtree_BST, left_sum, left_min, left_max = post_order(node.left)
            right_subtree_BST, right_sum, right_min, right_max = post_order(node.right)

            if left_subtree_BST and right_subtree_BST and left_max < node.val < right_min:
                current_sum = left_sum + node.val + right_sum
                self.maxSum = max(self.maxSum, current_sum)
                current_min = min(node.val, left_min)
                current_max = max(node.val, right_max)
                return True, current_sum, current_min, current_max
            
            return False, 0, 0, 0
        post_order(root)
        return self.maxSum