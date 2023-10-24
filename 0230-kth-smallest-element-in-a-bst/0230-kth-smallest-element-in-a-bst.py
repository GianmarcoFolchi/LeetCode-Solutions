# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    k = 0
    ans = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k 
        def bfs(root): 
            if not root or k < 0: 
                return 
            bfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                self.k = -1
            bfs(root.right)
        bfs(root)
        return self.ans