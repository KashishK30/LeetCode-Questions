# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## ITERATIVE WAY USING 2 STACK
        
        if not root:
            return

        result = []
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            
        while stack2:
            result.append(stack2.pop().val)

        return result


        ## RESURSIVE WAY

        # def post_order(node, result):
        #     if not node:
        #         return 
        #     post_order(node.left, result)
        #     post_order(node.right, result)
        #     result.append(node.val)

        # result = []
        # post_order(root, result)
        # return result