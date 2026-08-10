class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac_visited = set()
        at_visited = set()

        pac_queue = deque()
        at_queue = deque()

        def bfs(queue, visited):
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    curr_row, curr_col = queue.popleft()

                    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                    for delta_row, delta_col in directions:
                        next_row = curr_row + delta_row
                        next_col = curr_col + delta_col

                        if (0 <= next_row < rows and
                            0 <= next_col < cols and
                            (next_row, next_col) not in visited and
                            heights[next_row][next_col] >= heights[curr_row][ curr_col]):

                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))


        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pac_visited.add((r, c))
                    pac_queue.append((r, c))
                
                if r == rows - 1 or c == cols - 1:
                    at_visited.add((r, c))
                    at_queue.append((r, c))
        
        bfs(pac_queue, pac_visited)
        bfs(at_queue, at_visited)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac_visited and (row, col) in at_visited:
                    result.append([row, col])
            
        return result