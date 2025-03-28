# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def helper(node, is_root):
            if not node:
                return None
            # Determine if this node needs to be a root
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            # Recursively process the left and right subtrees
            node.left = helper(node.left, root_deleted)
            node.right = helper(node.right, root_deleted)
            # Return None if the current node needs to be deleted
            return None if root_deleted else node

        helper(root, True)
        return forest