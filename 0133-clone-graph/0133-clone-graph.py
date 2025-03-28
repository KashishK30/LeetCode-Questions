"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        queue = deque([node])

        old_to_new[node] = Node(node.val)

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)

                    queue.append(neighbor)

                old_to_new[current].neighbors.append(old_to_new[neighbor])
            
        return old_to_new[node]

        # if not node:
        #     return None

        # cloned_nodes = {}

        # def dfs(curr_node):
        #     if curr_node in cloned_nodes:
        #         return cloned_nodes[curr_node]
            
        #     clone = Node(curr_node.val)
        #     cloned_nodes[curr_node] = clone

        #     for neighbor in curr_node.neighbors:
        #         clone.neighbors.append(dfs(neighbor))

        #     return clone
        
        # return dfs(node)
        