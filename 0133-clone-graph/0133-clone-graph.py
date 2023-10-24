"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import queue 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return None
        copyMap = {}
        def dfs(node):
            if node in copyMap: 
                return copyMap[node]
            newNode = Node(node.val)
            copyMap[node] = newNode
            for neighbor in node.neighbors: 
                newNode.neighbors.append(dfs(neighbor))

            return newNode

        return dfs(node)

            



