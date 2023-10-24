class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums): 
            if i != 0 and nums[i-1] == num:
                continue 
            j, k = i + 1, len(nums) - 1 
            while j < k: 
                if nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
                    
        return ans 
                


    




