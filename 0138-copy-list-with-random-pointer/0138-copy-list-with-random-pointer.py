"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {}
        copyMap[None] = None
        def bfs(oldNode): 
            if oldNode in copyMap: 
                return copyMap[oldNode]
            newNode = Node(oldNode.val)
            copyMap[oldNode] = newNode
            newNode.next = bfs(oldNode.next)
            newNode.random = bfs(oldNode.random)
            return newNode
        
        return bfs(head)