class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        
        for i, num in enumerate(nums):
            dic.setdefault(num, []).append(i)
            
        for num in nums:
            currTarget = target - num
            if currTarget in dic:
                if currTarget == num:
                    if len(dic[num]) > 1:
                        return [dic[num][0], dic[num][1]]
                    else:
                        continue
                        
                return [dic[num][0], dic[currTarget][0]]
                    
                    
        
        

            
                
        
        
                
                