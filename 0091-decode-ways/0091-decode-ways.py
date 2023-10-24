class Solution:
    def numDecodings(self, s: str) -> int:
        numSet = set([str(i) for i in range(1, 27)])
        memo = {}
        memo[len(s)] = 1
        def decode(i): 
            if i in memo: 
                return memo[i]
            res = 0
            if s[i] in numSet:
                res += decode(i+1)
            if i + 2 <= len(s) and s[i:i+2] in numSet: 
                res += decode(i+2)
            memo[i] = res
            return res
        
        return decode(0)

    