import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        heap = []
        kClosestPoints = []
        for (x, y) in points: 
            heapq.heappush(heap, (distance(x, 0, y, 0), [x, y]))
        
        for i in range(k): 
            kClosestPoints.append(heapq.heappop(heap)[1])
        
        return kClosestPoints


def distance(x1: int, x2: int, y1: int, y2: int) -> int: 
    return sqrt((x1-x2) ** 2 + (y1 - y2) ** 2)