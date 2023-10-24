class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: 
            return False
        target = sum(nums) // 2
        sumSet = set() 
        sumSet.add(0)
        for num in nums: 
            if num == target: 
                return True
            nextSumSet = set()
            for possibleSum in sumSet: 
                nextSumSet.add(num + possibleSum)
                nextSumSet.add(possibleSum)
            sumSet = nextSumSet
            if target in sumSet: 
                return True

        return False

            