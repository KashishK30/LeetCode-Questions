# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLCA(self, p, q, root):
        if not root or root.val == p or root.val == q:
            return root
        left = self.findLCA(p, q, root.left)
        right = self.findLCA(p, q, root.right)

        if left and right:
            return root
        return left if left else right
    
    def findPath(self, root, target, path):
        if not root:
            return False
        if root.val == target:
            return True
        path.append('L')
        if self.findPath(root.left, target, path):
            return True
        path.pop()
        path.append('R')
        if self.findPath(root.right, target, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self.findLCA(startValue, destValue, root)

        pathToStart = []
        self.findPath(lca, startValue, pathToStart)

        pathToDest = []
        self.findPath(lca, destValue, pathToDest)

        result = ['U'] * len(pathToStart)

        result.extend(pathToDest)

        return ''.join(result)
    