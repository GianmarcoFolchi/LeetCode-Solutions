"""
All ways to go from src to dst in k steps 
                 3<-------
                 ^        |
                 | 600    |
                 |        | 200
           100   |  100.  |
        0 -----> 1 ------>2
        ^                |  
        |       100      |
        ------------------
        V^2 * log(V)
"""
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] [from, dst, price], src = 0, dst = 3, k = 1 n = 4
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edgeMap = defaultdict(list)
        visited = set()
        for (src1, dst1, price) in flights: 
            edgeMap[src1].append((price, dst1))
        heap = [(0, src, 0)] #(price, src, stops)
        while heap:
            price, loc, stops = heapq.heappop(heap)
            if (loc, stops) in visited:
                continue
            visited.add((loc, stops))
            if loc == dst and stops - 1 <= k: 
                return price
            if stops > k: 
                continue
            for (price1, dst1) in edgeMap[loc]: 
                heapq.heappush(heap, (price + price1, dst1, stops + 1))
    
        return -1

   
