class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations): 
          a, b = eq
          adj[a].append([b, values[i]])
          adj[b].append([a, 1/values[i]])
        def bfs(src, target): 
          if src not in adj or target not in adj: 
            return -1
          if src == target: 
            return 1
          q, seen = deque(), set()
          q.append([src, 1])
          seen.add(src)
          while len(q) > 0:
            curNode, weight = q.popleft() 
            for nei in adj[curNode]:
              node, w = nei
              if node == target: 
                return weight * w
              if node not in seen: 
                q.append([node, weight * w])
                seen.add(node)
          
          return -1 
        
        res = []
        for a, b in queries: 
          res.append(bfs(a, b))

        return res 