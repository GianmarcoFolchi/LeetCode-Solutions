class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
    # 1,4,2,3 test case 
    # 1,4,8,24 prefix 
    # 24,24,6,3 postfix
    # 24,6,12,8
        prefix = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
                continue 
            prefix[i] = prefix[i-1] * num
        
        postfix = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
                continue 
            postfix[i] = postfix[i+1] * nums[i]
        
        ans = [0 for _ in range(len(nums))]
        for i, num in enumerate(ans): 
            left = 1
            right = 1
            if i > 0:
                left = prefix[i-1]
            if i < len(nums) - 1:
                right = postfix[i+1]
            ans[i] = left * right
        return ans 
        
        

