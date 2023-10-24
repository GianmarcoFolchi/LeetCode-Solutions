"""
        if 2 same letters in row, reset and go to last
        if not in a row, then restart that the letter after first occurance
        to know if a letter is already in the sliding window, maintain a set 
        pwewkew
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dupSet = set()
        longestSub = 1
        l = 0
        for r, char in enumerate(s):
            if r == 0:
                dupSet.add(char)
                continue
            longestSub = max(longestSub, len(dupSet))
            if char in dupSet:
                while s[l] != char:
                    dupSet.remove(s[l])
                    l += 1
                l += 1
            else: 
                dupSet.add(char)
        
        longestSub = max(longestSub, len(dupSet))
        return longestSub 

            

    






