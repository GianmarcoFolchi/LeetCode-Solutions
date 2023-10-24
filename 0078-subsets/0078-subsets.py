class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, subset): 
            if i >= len(nums):
                result.append(subset.copy())
                return 
                
            backtrack(i + 1, subset)
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
        
        backtrack(0, [])
        return result