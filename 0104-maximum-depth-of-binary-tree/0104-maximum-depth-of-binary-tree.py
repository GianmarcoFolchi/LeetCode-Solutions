# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        def dfs(root): 
            l = 0
            r = 0
            if root.left: 
                l = dfs(root.left) + 1
            if root.right: 
                r = dfs(root.right) + 1
            
            return max(l, r)
        
        return 1 + dfs(root)