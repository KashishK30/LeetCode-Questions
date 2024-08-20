# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildBST(lower, upper):
            nonlocal index
            if index == len(preorder) or preorder[index] > upper or preorder[index] < lower:
                return None

            root_val = preorder[index]
            root = TreeNode(root_val)
            index += 1

            root.left = buildBST(lower, root_val)
            root.right = buildBST(root_val, upper)

            return root
        index = 0

        return buildBST(float('-inf'), float('inf'))