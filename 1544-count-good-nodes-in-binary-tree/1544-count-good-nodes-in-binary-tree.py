# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        result = 1
        def solver(root, curMax): 
            if not root: 
                return 0 
            result = 0 
            if root.val >= curMax: 
                curMax = root.val
                result += 1
            return result + solver(root.left, curMax) + solver(root.right, curMax)

        result += solver(root.left, root.val)
        result += solver(root.right, root.val)
        return result 
        