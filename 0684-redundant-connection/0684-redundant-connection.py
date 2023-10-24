class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Use the union find algorithm
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        res = edges[-1]
        for (a, b) in edges: 
            if union(par, rank, a - 1, b - 1) == -1: 
                res = [a, b]
        
        return res


def union(par, rank, a, b): 
    parA, parB = find(par, a), find(par, b)
    if parA == parB: #they are already joined
        return -1
    if rank[parA] > rank[parB]: 
        rank[parA] += 1
        par[parB] = parA
    else: 
        rank[parB] += 1
        par[parA] = parB
    return 1

def find(par, a): 
    curr = par[a]
    while curr != par[curr]: 
        curr = par[curr]
    return curr # might just need to return curr
            