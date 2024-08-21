# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## Recurssive

        def in_order_traversal(node):
            if node is None:
                return []

            left_values = in_order_traversal(node.left)

            current_value = [node.val]

            right_values = in_order_traversal(node.right)
            return left_values + current_value + right_values
        sorted_values = in_order_traversal(root)
        return sorted_values[k - 1]

        ## Iterative
        # stack = []
        # current = root
        # count = 0

        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     count += 1
        #     if count == k:
        #         return current.val
        #     current = current.right
        # return -1