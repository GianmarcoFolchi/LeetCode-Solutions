class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        result = 0 
        rectangleRatioMap = {}
        for (width, height) in rectangles: 
            ratio = width / height
            rectangleRatioMap[ratio] = rectangleRatioMap.get(ratio, -1) + 1
            result += rectangleRatioMap[ratio]
            
        return result