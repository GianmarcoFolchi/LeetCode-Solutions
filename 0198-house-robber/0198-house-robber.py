class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        memo = {}
        memo[len(nums)] = 0
        memo[len(nums) + 1] = 0
        memo[len(nums) + 2] = 0
        def solver(i): 
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(solver(i + 2), solver(i + 3))
            return memo[i]

        solver(0)
        solver(1)
        return max(memo[0], memo[1])