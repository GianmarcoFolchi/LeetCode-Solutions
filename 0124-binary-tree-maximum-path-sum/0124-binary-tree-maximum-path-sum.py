# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root): 
            if not root: 
                return 0 
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.ans = max(self.ans, root.val + left + right, root.val + max(left, right))
            return root.val + max(left, right)

        dfs(root)
        return self.ans