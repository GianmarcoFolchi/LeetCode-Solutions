class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = curSum = 0 
        prefixSum = {0: 1}
        for num in nums: 
            curSum += num
            result += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        
        return result