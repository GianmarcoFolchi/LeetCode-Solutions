#create a mean heap of all connections in tree
#pop from tree, and use union find to check if that connection will connect a new unconnected node
#check if connected points == number points
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        unconnectedComponents = len(points)
        par = [i for i in range(len(points))]
        rank = [0] * len(points)
        cost = 0 
        for i in range(len(points)): 
            for j in range(i + 1, len(points)): 
                distance = getDistance(points[i][0], points[i][1], points[j][0], points[j][1])
                heapq.heappush(heap, (distance, i, j))
        
        while heap and unconnectedComponents > 0: 
            distance, i, j = heapq.heappop(heap)
            if union(par, rank, i, j) == 1: 
                unconnectedComponents -= 1
                cost += distance
            
        return cost

def union(par, rank, p1, p2): 
    p1, p2 = find(par, p1), find(par, p2)
    if p1 == p2: 
        return 0
    if rank[p1] > rank[p2]: 
        par[p2] = p1
    else: 
        par[p1] = p2

    return 1

def find(par, p1): 
    cur = par[p1]
    while cur != par[cur]: 
        cur = par[cur]
    return cur


def getDistance(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)