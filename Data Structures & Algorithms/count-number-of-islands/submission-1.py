class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            directions = [ [1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                dfs(dr + r, dc + c)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)


        return islands