class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        #  0,1,2,3,4,5,6,7,8
        #  area = min(height i and j) * j - i 
        maxWater = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxWater = max(maxWater, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxWater