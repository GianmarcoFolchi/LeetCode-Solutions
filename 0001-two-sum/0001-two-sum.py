class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, num in enumerate(nums): 
            indexMap[num] = i
        
        for i, num in enumerate(nums): 
            if target - num in indexMap and indexMap[target - num] != i:
                return [i, indexMap[target - num]]