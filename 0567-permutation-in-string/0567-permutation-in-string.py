from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = dict(Counter(s1))
        s2Map = {}
        l = 0 
        have, need = 0, len(s1Map)
        for i, char in enumerate(s2): 
            if char not in s1Map: 
                l = i + 1
                s2Map.clear()
                continue 

            s2Map[char] = s2Map.get(char, 0) + 1
            if s2Map[char] > s1Map[char]: 
                while s2[l] != char: 
                    s2Map[s2[l]] -= 1 
                    if s2Map[s2[l]] <= 0: 
                        del s2Map[s2[l]]
                    l += 1
                s2Map[s2[l]] -= 1 
                if s2Map[s2[l]] <= 0: 
                    del s2Map[s2[l]]
                l += 1
            if len(s2Map) == len(s1Map) and s2Map == s1Map: 
                return True

        return False