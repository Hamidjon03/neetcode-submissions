class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # look throug every single cell
        # if cell is 1 call the function wich compute and change land to water 
        # if cell is 1 increase count_land by 1
        # return count_land


        ROWS = len(grid)
        COLS = len(grid[0])
        count_land = 0

        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        def change_to_water(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                change_to_water(r + dr, c + dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count_land += 1
                    change_to_water(i, j)
        
        return count_land

