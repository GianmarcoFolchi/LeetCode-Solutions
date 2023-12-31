class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, visited): 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
                return 
            visited.add((i, j))
            dfs(i + 1, j, visited)
            dfs(i - 1, j, visited)
            dfs(i, j + 1, visited)
            dfs(i, j - 1, visited)

        visited = set()
        islands = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    islands += 1

        return islands