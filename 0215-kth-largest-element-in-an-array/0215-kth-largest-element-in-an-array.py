class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums): 
            return float('-inf')
        freqCounter = dict(Counter(nums))
        for i in range(max(nums), min(nums) - 1, -1):
            k -= freqCounter.get(i, 0)
            if k <= 0: 
                return i