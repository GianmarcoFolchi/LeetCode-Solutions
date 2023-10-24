class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1): 
            maxIncreasing = 0
            for j in range(i + 1, len(nums)): 
                maxIncreasing = max(maxIncreasing, dp[j] if nums[j] > nums[i] else 0)
            dp[i] += maxIncreasing
        
        return max(dp)