class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        timeMap = {} #node : timeToReach
        edgeMap = defaultdict(list) # par: [(dest, weight)]
        heap = [(0, k)] #(timeToReach,  node)
        t = 0
        for (start, dest, weight) in times: 
            edgeMap[start].append((weight, dest))
        
        while heap and len(timeMap) < n:
            timeToReach, node = heapq.heappop(heap)
            if node in timeMap: 
                continue 
            timeMap[node] = timeToReach
            t = max(t, timeToReach)
            for (weight, dest) in edgeMap[node]: 
                if dest not in timeMap:
                    heapq.heappush(heap, (timeToReach + weight, dest))

        return t if len(timeMap) == n else -1