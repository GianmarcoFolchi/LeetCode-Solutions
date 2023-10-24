class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def solver(nums, currSum, i):
            if currSum == target:
                self.res.append(nums.copy())
                return 
            for j in range(i, len(candidates)):
                if currSum + candidates[j] <= target:
                    nums.append(candidates[j])
                    solver(nums, currSum + candidates[j], j)
                    nums.pop()


        for i in range(len(candidates)):
            solver([candidates[i]], candidates[i], i)
        
        return self.res
