class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        numSet = set(nums)
        print(numSet)
        maxStreak = 1
        for num in numSet: 
            currStreak = 1
            if num - 1 not in numSet: 
                currNum = num + 1
                while currNum in numSet: 
                    currStreak += 1 
                    currNum += 1
                    maxStreak = max(maxStreak, currStreak)

        return maxStreak