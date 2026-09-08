class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
# bfs solution using visit set
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    grid[nr][nc] == '0' or
                    (nr, nc) in visit
                    ):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

''' # dfs solution using visit set
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or 
            r == ROWS or c == COLS or 
            grid[r][c] == '0' or 
            (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc) 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands
'''

        