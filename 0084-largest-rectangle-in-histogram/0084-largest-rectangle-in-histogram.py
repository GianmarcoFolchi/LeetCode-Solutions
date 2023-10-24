class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights): 
            smallerIndex = i 
            while stack and height < stack[-1].height: 
                smallerHeight, smallerIndex = stack[-1].height, stack[-1].index
                stack.pop()
                maxArea = max(maxArea, smallerHeight * (i - smallerIndex))
            stack.append(RectangleNode(height, smallerIndex))
        
        for node in stack: 
            maxArea = max(maxArea, node.height * (len(heights) - node.index))
        
        return maxArea
        
class RectangleNode: 
    def __init__(self, height, index): 
        self.index = index
        self.height = height 