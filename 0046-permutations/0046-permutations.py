class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(used, perm): 
            if len(perm) == len(used): 
                result.append(perm.copy())

            for i in range(len(used)): 
                if used[i]: 
                    continue 
                perm.append(nums[i])
                used[i] = True
                backtrack(used, perm)
                used[i] = False
                perm.pop()
        
        backtrack([False] * len(nums), [])
        return result
                