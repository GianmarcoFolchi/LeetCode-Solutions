class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def backtrack(perm): 
            if len(perm) == len(used): 
                result.append(perm.copy())
                return 

            for i in range(len(used)): 
                if used[i]: 
                    continue 
                perm.append(nums[i])
                used[i] = True
                backtrack(perm)
                used[i] = False
                perm.pop()
        
        backtrack([])
        return result
                