# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ITERATIVE SOLUTION
        if not root:
            return
        
        result = []

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

        # RECURSIVE SOLUTION
        #  def preorder(node, result):
        #     if not node:
        #         return 
        #     result.append(node.val)
        #     preorder(node.left, result)
        #     preorder(node.right, result)
        
        # result = []
        # preorder(root, result)
        # return result
            