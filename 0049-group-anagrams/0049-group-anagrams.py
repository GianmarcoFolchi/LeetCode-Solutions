class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        sortedStrs = strs.copy()
        for i, str in enumerate(sortedStrs):
            sortedStrs[i] = ''.join(sorted(str))
        
        for i, str in enumerate(sortedStrs): 
            anagramGroups[str].append(strs[i])

        return anagramGroups.values()
        
