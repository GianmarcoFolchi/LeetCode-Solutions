class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []
        result = 0 
        for i, h in enumerate(height): 
            if i == 0: 
                maxLeft.append(h)
                continue
            maxLeft.append(max(maxLeft[i - 1], h))
        
        for i in range(len(height) - 1, -1, -1): 
            if i == len(height) - 1: 
                maxRight.append(height[i])
                continue
            maxRight.append(max(maxRight[-1], height[i]))
        maxRight.reverse()
        
        for i, h in enumerate(height): 
            result += min(maxLeft[i], maxRight[i]) - h if min(maxLeft[i], maxRight[i]) - h >= 0 else 0 
        
        return result


        